from faker import Faker
from datetime import datetime
from tables import Invoice
from setup import session
import random
import json

NUM_RECORDS = 50

fake = Faker()

CATEGORIES = [
    "Office Supplies",
    "Software & Technology",
    "Marketing & Advertising",
    "Travel & Transportation",
    "Meals & Entertainment",
    "Professional Services",
    "Utilities",
    "Equipment & Hardware",
    "Training & Education",
    "Maintenance & Repairs",
]


def generate_invoice_number():
    """Generate a realistic invoice number"""
    prefix = random.choice(["INV", "BILL", "RCP"])
    year = datetime.now().year
    number = fake.random_int(min=1000, max=9999)
    return f"{prefix}-{year}-{number:04d}"


def generate_items_services():
    """Generate realistic items/services JSON data"""
    num_items = random.randint(1, 5)
    items = []

    for _ in range(num_items):
        item = {
            "description": fake.catch_phrase(),
            "quantity": random.randint(1, 10),
            "unit_price": round(random.uniform(10.0, 500.0), 2),
            "total": 0,
        }
        item["total"] = round(item["quantity"] * item["unit_price"], 2)
        items.append(item)

    return items


def generate_merchant_address():
    """Generate a complete merchant address"""
    return (
        f"{fake.street_address()}, {fake.city()}, {fake.state_abbr()} {fake.zipcode()}"
    )


def create_invoice_data():
    """Create a single invoice record"""
    return {
        "invoice_number": generate_invoice_number(),
        "invoice_date": fake.date_between(start_date="-2y", end_date="today"),
        "category": random.choice(CATEGORIES),
        "merchant_name": fake.company(),
        "merchant_address": generate_merchant_address(),
        "items_services": generate_items_services(),
        "remark": fake.text(max_nb_chars=200) if random.choice([True, False]) else None,
    }


def seed_invoices():
    try:
        print(f"Starting to generate {NUM_RECORDS} invoice records...")

        invoices = []
        for i in range(NUM_RECORDS):
            invoice_data = create_invoice_data()
            invoice = Invoice(**invoice_data)
            invoices.append(invoice)

            # Print progress every 10 records
            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1}/{NUM_RECORDS} records...")

        session.add_all(invoices)
        session.commit()

        print(f"Successfully seeded {NUM_RECORDS} invoice records!")

    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()


def preview_sample_data():
    """Preview sample data without inserting to database"""
    print("Sample Invoice Data:")
    print("-" * 50)

    for i in range(3):
        data = create_invoice_data()
        print(f"Invoice {i + 1}:")
        print(f"  Number: {data['invoice_number']}")
        print(f"  Date: {data['invoice_date']}")
        print(f"  Category: {data['category']}")
        print(f"  Merchant: {data['merchant_name']}")
        print(f"  Address: {data['merchant_address']}")
        print(f"  Items: {len(data['items_services'])} items")
        print(f"  Remark: {data['remark'][:50] + '...' if data['remark'] else 'None'}")
        print(f"  Items/Services: {json.dumps(data['items_services'], indent=2)}")
        print("-" * 50)


if __name__ == "__main__":
    seed_invoices()
