"""
Create random mock data of claims based on NUM_RECORDS
MUST RUN AFTER seeder_employee.py and seeder_invoice.py
Due to Foreign keys
"""

from faker import Faker
from datetime import datetime, timedelta
import random
from decimal import Decimal
from setup import session
from tables import Invoice, Employee, Claim

NUM_RECORDS = 75

fake = Faker()

CLAIM_TYPES_REASONS = {
    "Travel Expense": [
        "Business trip to client site",
        "Conference attendance travel costs",
        "Training seminar travel expenses",
        "Customer meeting travel",
        "Team building event travel",
    ],
    "Meal Allowance": [
        "Client dinner meeting",
        "Working lunch during overtime",
        "Business conference meals",
        "Team meeting catering",
        "Late night work meal",
    ],
    "Office Supplies": [
        "Urgent office supplies purchase",
        "Home office equipment for remote work",
        "Project-specific materials",
        "Replacement of damaged equipment",
        "Additional supplies for team expansion",
    ],
    "Software License": [
        "Professional development software",
        "Project management tool subscription",
        "Design software license renewal",
        "Security software purchase",
        "Productivity tool subscription",
    ],
    "Training & Education": [
        "Professional certification course",
        "Industry conference registration",
        "Online training platform subscription",
        "Workshop attendance fee",
        "Skills development program",
    ],
    "Equipment Purchase": [
        "Laptop replacement for work",
        "Monitor for improved productivity",
        "Ergonomic office chair",
        "Mobile device for field work",
        "Specialized tools for project",
    ],
    "Transportation": [
        "Taxi fare for client meeting",
        "Parking fees during business trip",
        "Public transport for work travel",
        "Ride-sharing for late work",
        "Vehicle rental for business use",
    ],
    "Communication": [
        "Mobile phone bill reimbursement",
        "Internet upgrade for remote work",
        "International calling charges",
        "Video conferencing software",
        "Communication equipment purchase",
    ],
}

CLAIM_STATUSES = {
    "Pending": 0.30,
    "Approved": 0.50,
    "Rejected": 0.20,
}


def generate_claim_number():
    """Generate a unique claim number"""
    prefix = "CLM"
    year = datetime.now().year
    number = fake.random_int(min=1000, max=9999)
    return f"{prefix}-{year}-{number:04d}"


def generate_claim_type_and_reason():
    """Generate a claim type and corresponding reason"""
    claim_type = random.choice(list(CLAIM_TYPES_REASONS.keys()))
    reason = random.choice(CLAIM_TYPES_REASONS[claim_type])
    return claim_type, reason


def generate_claim_amount(claim_type):
    """Generate realistic claim amount based on claim type"""
    amount_ranges = {
        "Travel Expense": (200, 2000),
        "Meal Allowance": (25, 150),
        "Office Supplies": (50, 500),
        "Software License": (100, 1500),
        "Training & Education": (300, 3000),
        "Equipment Purchase": (500, 5000),
        "Transportation": (20, 200),
        "Communication": (50, 300),
    }

    min_amount, max_amount = amount_ranges.get(claim_type, (50, 500))
    amount = random.uniform(min_amount, max_amount)
    return Decimal(str(round(amount, 2)))


def generate_status():
    """Generate status based on weighted probabilities"""
    statuses = list(CLAIM_STATUSES.keys())
    weights = list(CLAIM_STATUSES.values())
    return random.choices(statuses, weights=weights)[0]


def generate_dates(status):
    """Generate submitted_date and reviewed_date based on status"""
    submitted_date = fake.date_between(start_date="-6M", end_date="today")

    reviewed_date = None
    if status in ["Approved", "Rejected"]:
        start_review = submitted_date + timedelta(days=1)
        end_review = min(submitted_date + timedelta(days=30), datetime.now().date())
        reviewed_date = fake.date_between(start_date=start_review, end_date=end_review)

    return submitted_date, reviewed_date


def generate_resolution(status):
    """Generate resolution text based on status"""
    resolutions = {
        "Approved": [
            "Claim approved as per company policy. Amount will be processed in next payroll.",
            "Valid business expense. Approved for reimbursement.",
            "Documentation verified. Claim approved for payment.",
            "Expense justified and within policy limits. Approved.",
            "All requirements met. Claim approved for processing.",
        ],
        "Rejected": [
            "Insufficient documentation provided. Please resubmit with proper receipts.",
            "Expense exceeds policy limits. Claim rejected.",
            "Not a valid business expense as per company policy.",
            "Missing required approvals. Claim cannot be processed.",
            "Expense not pre-approved as required by policy.",
        ],
        "Paid": [
            "Claim processed and payment completed on [date].",
            "Reimbursement transferred to employee account.",
            "Payment processed successfully. Transaction ID: TXN"
            + str(fake.random_int(min=100000, max=999999)),
            "Amount paid via direct deposit.",
            "Claim settled. Payment confirmation sent to employee.",
        ],
    }

    if status in resolutions:
        return random.choice(resolutions[status])
    return None


def get_valid_foreign_keys(session):
    """Get valid invoice and employee IDs from the database"""
    try:
        # Get all invoice IDs
        invoice_ids = session.query(Invoice.id).all()
        invoice_ids = [id[0] for id in invoice_ids] if invoice_ids else []

        # Get all employee IDs
        employee_ids = session.query(Employee.id).all()
        employee_ids = [id[0] for id in employee_ids] if employee_ids else []

        return invoice_ids, employee_ids
    except Exception as e:
        print(f"Error fetching foreign keys: {e}")
        return [], []


def create_claim_data(invoice_ids, employee_ids):
    """Create a single claim record"""
    if not invoice_ids or not employee_ids:
        raise ValueError(
            "No valid invoice or employee IDs found. Please seed invoices and employees first."
        )

    claim_type, reason = generate_claim_type_and_reason()
    status = generate_status()
    submitted_date, reviewed_date = generate_dates(status)

    return {
        "claim_number": generate_claim_number(),
        "invoice_id": random.choice(invoice_ids),
        "employee_id": random.choice(employee_ids),
        "claim_type": claim_type,
        "claim_amount": generate_claim_amount(claim_type),
        "reason": reason,
        "status": status,
        "submitted_date": submitted_date,
        "reviewed_date": reviewed_date,
        "resolution": generate_resolution(status),
    }


def seed_claims():
    try:
        print("Fetching valid invoice and employee IDs...")
        invoice_ids, employee_ids = get_valid_foreign_keys(session)

        if not invoice_ids:
            print("No invoices found! Please run the invoice seeder first.")
            return

        if not employee_ids:
            print("No employees found! Please run the employee seeder first.")
            return

        print(f"Found {len(invoice_ids)} invoices and {len(employee_ids)} employees")
        print(f"Starting to generate {NUM_RECORDS} claim records...")

        claims = []
        used_claim_numbers = set()

        for i in range(NUM_RECORDS):
            # Ensure unique claim numbers
            attempts = 0
            while attempts < 10:
                claim_data = create_claim_data(invoice_ids, employee_ids)

                if claim_data["claim_number"] not in used_claim_numbers:
                    used_claim_numbers.add(claim_data["claim_number"])
                    break
                attempts += 1

            if attempts >= 10:
                print(
                    f"Warning: Could not generate unique claim number for record {i + 1}"
                )
                continue

            claim = Claim(**claim_data)
            claims.append(claim)

            # Print progress every 10 records
            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1}/{NUM_RECORDS} records...")

        session.add_all(claims)
        session.commit()

        print(f"Successfully seeded {len(claims)} claim records!")

        print_claim_statistics(claims)

    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()


def print_claim_statistics(claims):
    """Print statistics about generated claims"""
    print("\nClaim Statistics:")
    print("-" * 50)

    status_counts = {}
    type_counts = {}
    total_amount = Decimal("0")

    for claim in claims:
        status_counts[claim.status] = status_counts.get(claim.status, 0) + 1
        type_counts[claim.claim_type] = type_counts.get(claim.claim_type, 0) + 1
        total_amount += claim.claim_amount

    print("Status Distribution:")
    for status, count in status_counts.items():
        percentage = (count / len(claims)) * 100
        print(f"  {status}: {count} ({percentage:.1f}%)")

    print(f"\nTotal Claim Amount: ${total_amount:,.2f}")
    print(f"Average Claim Amount: ${total_amount / len(claims):,.2f}")

    print("\nTop Claim Types:")
    sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
    for claim_type, count in sorted_types[:5]:
        print(f"  {claim_type}: {count}")


def preview_sample_data():
    """Preview sample data without inserting to database"""
    print("Sample Claim Data:")
    print("-" * 80)

    mock_invoice_ids = [1, 2, 3, 4, 5]
    mock_employee_ids = [1, 2, 3, 4, 5]

    for i in range(3):
        data = create_claim_data(mock_invoice_ids, mock_employee_ids)
        print(f"Claim {i + 1}:")
        print(f"  Number: {data['claim_number']}")
        print(f"  Invoice ID: {data['invoice_id']}")
        print(f"  Employee ID: {data['employee_id']}")
        print(f"  Type: {data['claim_type']}")
        print(f"  Amount: ${data['claim_amount']}")
        print(f"  Reason: {data['reason']}")
        print(f"  Status: {data['status']}")
        print(f"  Submitted: {data['submitted_date']}")
        print(f"  Reviewed: {data['reviewed_date']}")
        print(f"  Resolution: {data['resolution']}")
        print("-" * 80)


if __name__ == "__main__":
    # preview_sample_data()
    seed_claims()
