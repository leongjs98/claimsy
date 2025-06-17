"""
Create random mock data of employees based on NUM_RECORDS
"""

from faker import Faker
import random
import hashlib
from decimal import Decimal
from setup import session
from tables import Employee

user_password="testtest"
NUM_RECORDS = 2

fake = Faker()

DEPARTMENTS_JOBS = {
    "Engineering": [
        "Software Engineer",
        "Senior Software Engineer",
        "Lead Developer",
        "DevOps Engineer",
        "QA Engineer",
        "Technical Lead",
        "Engineering Manager",
    ],
    "Marketing": [
        "Marketing Specialist",
        "Digital Marketing Manager",
        "Content Creator",
        "SEO Specialist",
        "Marketing Director",
        "Brand Manager",
        "Social Media Manager",
    ],
    "Sales": [
        "Sales Representative",
        "Account Manager",
        "Sales Manager",
        "Business Development Manager",
        "Sales Director",
        "Inside Sales Rep",
    ],
    "Human Resources": [
        "HR Specialist",
        "HR Manager",
        "Recruiter",
        "HR Director",
        "Training Coordinator",
        "HR Business Partner",
    ],
    "Finance": [
        "Accountant",
        "Financial Analyst",
        "Finance Manager",
        "CFO",
        "Accounts Payable Specialist",
        "Financial Controller",
        "Budget Analyst",
    ],
    "Operations": [
        "Operations Manager",
        "Project Manager",
        "Operations Analyst",
        "Supply Chain Manager",
        "Operations Director",
        "Process Improvement Specialist",
    ],
    "Customer Support": [
        "Customer Support Representative",
        "Support Manager",
        "Technical Support Specialist",
        "Customer Success Manager",
        "Support Team Lead",
    ],
    "Design": [
        "UI/UX Designer",
        "Graphic Designer",
        "Product Designer",
        "Creative Director",
        "Visual Designer",
        "Design Manager",
    ],
}


def generate_employee_id():
    """Generate a unique employee ID"""
    prefix = "EMP"
    number = fake.random_int(min=1000, max=9999)
    return f"{prefix}{number:04d}"


def generate_password_hash(password=user_password):
    """Generate a simple password hash (use proper hashing in production)"""
    return hashlib.sha256(password.encode()).hexdigest()


def generate_salary_by_job_title(job_title):
    """Generate realistic salary based on job title"""
    salary_ranges = {
        # Engineering
        "Software Engineer": (70000, 95000),
        "Senior Software Engineer": (95000, 130000),
        "Lead Developer": (120000, 160000),
        "DevOps Engineer": (80000, 120000),
        "QA Engineer": (60000, 85000),
        "Technical Lead": (130000, 170000),
        "Engineering Manager": (140000, 200000),
        # Marketing
        "Marketing Specialist": (45000, 65000),
        "Digital Marketing Manager": (65000, 90000),
        "Content Creator": (40000, 60000),
        "SEO Specialist": (50000, 75000),
        "Marketing Director": (100000, 150000),
        "Brand Manager": (70000, 100000),
        "Social Media Manager": (45000, 70000),
        # Sales
        "Sales Representative": (40000, 70000),
        "Account Manager": (60000, 90000),
        "Sales Manager": (80000, 120000),
        "Business Development Manager": (70000, 110000),
        "Sales Director": (120000, 180000),
        "Inside Sales Rep": (35000, 55000),
        # HR
        "HR Specialist": (45000, 65000),
        "HR Manager": (70000, 100000),
        "Recruiter": (50000, 75000),
        "HR Director": (100000, 150000),
        "Training Coordinator": (45000, 65000),
        "HR Business Partner": (80000, 120000),
        # Finance
        "Accountant": (45000, 70000),
        "Financial Analyst": (60000, 85000),
        "Finance Manager": (80000, 120000),
        "CFO": (150000, 300000),
        "Accounts Payable Specialist": (35000, 50000),
        "Financial Controller": (90000, 130000),
        "Budget Analyst": (55000, 80000),
        # Operations
        "Operations Manager": (70000, 110000),
        "Project Manager": (70000, 100000),
        "Operations Analyst": (55000, 80000),
        "Supply Chain Manager": (75000, 110000),
        "Operations Director": (120000, 180000),
        "Process Improvement Specialist": (65000, 95000),
        # Customer Support
        "Customer Support Representative": (30000, 45000),
        "Support Manager": (60000, 85000),
        "Technical Support Specialist": (45000, 65000),
        "Customer Success Manager": (65000, 95000),
        "Support Team Lead": (55000, 80000),
        # Design
        "UI/UX Designer": (60000, 90000),
        "Graphic Designer": (40000, 65000),
        "Product Designer": (80000, 120000),
        "Creative Director": (100000, 150000),
        "Visual Designer": (50000, 75000),
        "Design Manager": (90000, 130000),
    }

    min_salary, max_salary = salary_ranges.get(job_title, (40000, 80000))
    return Decimal(str(random.randint(min_salary, max_salary)))


def generate_department_and_job():
    """Generate a department and corresponding job title"""
    department = random.choice(list(DEPARTMENTS_JOBS.keys()))
    job_title = random.choice(DEPARTMENTS_JOBS[department])
    return department, job_title


def generate_phone_number():
    """Generate a realistic phone number"""
    return fake.phone_number()


def create_employee_data():
    """Create a single employee record"""
    department, job_title = generate_department_and_job()
    first_name = fake.first_name()
    last_name = fake.last_name()

    return {
        "employee_id": generate_employee_id(),
        "name": f"{first_name} {last_name}",
        "email": fake.email(),
        "password_hash": generate_password_hash(),
        "phone": generate_phone_number(),
        "department": department,
        "job_title": job_title,
        "hire_date": fake.date_between(start_date="-5y", end_date="today"),
        "salary": generate_salary_by_job_title(job_title),
    }


def seed_employees():
    try:
        print(f"Starting to generate {NUM_RECORDS} employee records...")

        employees = []
        used_employee_ids = set()
        used_emails = set()

        for i in range(NUM_RECORDS):
            attempts = 0
            while attempts < 10:
                employee_data = create_employee_data()

                if (
                    employee_data["employee_id"] not in used_employee_ids
                    and employee_data["email"] not in used_emails
                ):
                    used_employee_ids.add(employee_data["employee_id"])
                    used_emails.add(employee_data["email"])
                    break
                attempts += 1

            if attempts >= 10:
                print(f"Warning: Could not generate unique data for record {i + 1}")
                continue

            employee = Employee(**employee_data)
            employees.append(employee)

            # Print progress every 10 records
            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1}/{NUM_RECORDS} records...")

        session.add_all(employees)
        session.commit()

        print(f"Successfully seeded {len(employees)} employee records!")

    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()


def preview_sample_data():
    """Preview sample data without inserting to database"""
    print("Sample Employee Data:")
    print("-" * 80)

    for i in range(3):
        data = create_employee_data()
        print(f"Employee {i + 1}:")
        print(f"  ID: {data['employee_id']}")
        print(f"  Name: {data['name']}")
        print(f"  Email: {data['email']}")
        print(f"  Phone: {data['phone']}")
        print(f"  Department: {data['department']}")
        print(f"  Job Title: {data['job_title']}")
        print(f"  Hire Date: {data['hire_date']}")
        print(f"  Salary: ${data['salary']:,}")
        print(f"  Password Hash: {data['password_hash'][:20]}...")
        print("-" * 80)


def generate_department_summary():
    """Generate a summary of departments and job titles"""
    print("Department and Job Title Summary:")
    print("-" * 50)
    for dept, jobs in DEPARTMENTS_JOBS.items():
        print(f"{dept}:")
        for job in jobs:
            print(f"  - {job}")
        print()


if __name__ == "__main__":
    seed_employees()
