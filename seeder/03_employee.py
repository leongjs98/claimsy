import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from faker import Faker
import random
from datetime import date, timedelta
from decimal import Decimal
import hashlib
from backend.db.tables import Employee
from backend.db.postgresql_setup import session

NUM_EMPLOYEES = 20
EMPLOYEE_PASSWORD = "testtest"

fake = Faker()

DEPARTMENTS = [
    "Engineering",
    "Marketing",
    "Sales",
    "Human Resources",
    "Finance",
    "Operations",
    "Customer Support",
    "Product Management",
    "Design",
    "Legal",
]

JOB_TITLES = {
    "Engineering": [
        "Software Engineer",
        "Senior Software Engineer",
        "Lead Engineer",
        "Engineering Manager",
        "DevOps Engineer",
    ],
    "Marketing": [
        "Marketing Specialist",
        "Marketing Manager",
        "Content Creator",
        "SEO Specialist",
        "Brand Manager",
    ],
    "Sales": [
        "Sales Representative",
        "Account Manager",
        "Sales Manager",
        "Business Development",
        "Sales Director",
    ],
    "Human Resources": [
        "HR Specialist",
        "HR Manager",
        "Recruiter",
        "HR Business Partner",
        "Talent Acquisition",
    ],
    "Finance": [
        "Financial Analyst",
        "Accountant",
        "Finance Manager",
        "Controller",
        "CFO",
    ],
    "Operations": [
        "Operations Specialist",
        "Operations Manager",
        "Process Analyst",
        "Supply Chain Manager",
    ],
    "Customer Support": [
        "Support Specialist",
        "Customer Success Manager",
        "Support Team Lead",
        "Technical Support",
    ],
    "Product Management": [
        "Product Manager",
        "Senior Product Manager",
        "Product Owner",
        "Product Director",
    ],
    "Design": [
        "UI/UX Designer",
        "Graphic Designer",
        "Product Designer",
        "Design Manager",
    ],
    "Legal": ["Legal Counsel", "Paralegal", "Compliance Officer", "Legal Manager"],
}

SALARY_RANGES = {
    "Engineering": (70000, 150000),
    "Marketing": (45000, 120000),
    "Sales": (40000, 130000),
    "Human Resources": (50000, 110000),
    "Finance": (55000, 140000),
    "Operations": (45000, 115000),
    "Customer Support": (35000, 80000),
    "Product Management": (80000, 160000),
    "Design": (50000, 120000),
    "Legal": (70000, 180000),
}


def hash_password(password: str) -> str:
    """Hash a password using hashlib"""
    return hashlib.sha256(password.encode()).hexdigest()


def generate_employee_id(index: int) -> str:
    """Generate employee ID in format EMP001, EMP002, etc."""
    return f"EMP{index:03d}"


def generate_hire_date() -> date:
    """Generate a random hire date within the last 5 years"""
    start_date = date.today() - timedelta(days=5 * 365)
    end_date = date.today() - timedelta(days=30)  # At least 30 days ago

    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)

    return start_date + timedelta(days=random_days)


def create_employee_data(index: int) -> dict:
    """Create a single employee's data"""
    department = random.choice(DEPARTMENTS)
    job_title = random.choice(JOB_TITLES[department])
    salary_min, salary_max = SALARY_RANGES[department]

    # Generate unique email
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    email = f"{first_name}.{last_name}@company.com"

    return {
        "employee_id": generate_employee_id(index + 1),
        "name": f"{first_name.title()} {last_name.title()}",
        "email": email,
        "password_hash": hash_password(EMPLOYEE_PASSWORD),
        "phone": fake.phone_number()[:20],  # Limit to 20 characters
        "department": department,
        "job_title": job_title,
        "hire_date": generate_hire_date(),
        "salary": Decimal(str(random.randint(salary_min, salary_max))),
    }


def seed_employees():
    """Seed the database with employee data"""
    try:
        print(f"Creating {NUM_EMPLOYEES} employees...")

        employees = []
        used_emails = set()
        used_employee_ids = set()

        for i in range(NUM_EMPLOYEES):
            while True:
                employee_data = create_employee_data(i)

                # Ensure unique email and employee_id
                if (employee_data["email"] not in used_emails and 
                    employee_data["employee_id"] not in used_employee_ids):
                    used_emails.add(employee_data["email"])
                    used_employee_ids.add(employee_data["employee_id"])
                    break

            employee = Employee(**employee_data)
            employees.append(employee)

            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1} employees...")

        session.add_all(employees)
        session.commit()

        print(f"Successfully seeded {NUM_EMPLOYEES} employees!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding employees: {e}")
    finally:
        session.close()

def show_help():
    """Show usage instructions"""
    print("Employee Seeder")
    print("=" * 50)
    print("Usage:")
    print("  python cleaner.py --number 30        - Seed 30 number of employees (DEFAULT: 20)")
    print("  python cleaner.py -n 30             - Shorcut for above")
    print("  python cleaner.py --help             - Show this help message")
    print("  python cleaner.py -h                 - Shortcut for above")
    print()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        seed_employees()
    elif len(sys.argv) == 2 and sys.argv[1] in ['--help', '-h']:
        show_help()
    elif len(sys.argv) == 3 and sys.argv[1] in ['--number', '-n']:
        try:
            NUM_EMPLOYEES = int(sys.argv[2])
            seed_employees()
        except ValueError:
            print("Error: Please provide a valid number")
            show_help()
    else:
        # Invalid arguments
        print("Error: Invalid arguments")
        show_help()
