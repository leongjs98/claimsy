"""
Create random mock data of claims based on NUM_RECORDS
MUST RUN AFTER seeder_employee.py and seeder_invoice.py
Due to Foreign keys
"""

import os
import sys
from typing import List
import json
from faker import Faker
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db.tables import Employee, Invoice, Claim
from backend.db.postgresql_setup import session
from backend.db.values import categories

fake = Faker()

NUM_CLAIMS = 20
MIN_NUM_CLAIM_FOR_EMPLOYEE_ID_1 = 20
claim_types = list(categories)
claim_types.append("Mixed")
statuses = ["pending", "approved", "rejected"]


def find_invoices_of_random_employee():
    # Get existing employees and invoices from the database
    employees = session.query(Employee).all()

    if not employees:
        print("No employees found. Please seed employees first.")
        return Employee(), List[Invoice()]

    selected_employee = random.choice(employees)
    invoices = (
        session.query(Invoice)
        .filter(Invoice.employee_id == selected_employee.id)
        .filter(Invoice.claim_id.is_(None))
        .all()
    )

    return selected_employee, invoices


def seed_claims_for_employee_id_1():
    employee_1 = session.query(Employee).filter(Employee.id == 1).first()
    try:
        for i in range(MIN_NUM_CLAIM_FOR_EMPLOYEE_ID_1):
            invoices = (
                session.query(Invoice)
                .filter(Invoice.employee_id == 1)
                .filter(Invoice.claim_id.is_(None))
                .all()
            )
            selected_invoices = List[Invoice]

            status = random.choices(statuses, weights=[10, 60, 30], k=1)[0]
            claim = Claim(
                claim_number=f"CLM-{fake.unique.random_number(digits=8)}",
                employee_id=1,
                claim_type=random.choice(claim_types),
                reason=fake.text(max_nb_chars=200),
                status=status,
                submitted_date=fake.date_between(start_date="-1y", end_date="today"),
                reviewed_date=fake.date_between(start_date="-6m", end_date="today")
                if random.choice([True, False])
                else None,
                resolution=fake.text(max_nb_chars=150)
                if random.choice([True, False])
                else None,
                is_anomaly=random.random() < 0.7 if status == "rejected" else False,
            )

            # Randomly assign 1-3 invoices to each claim using actual invoice IDs
            num_invoices_to_assign = random.randint(1, min(3, len(invoices)))
            if num_invoices_to_assign > 5:
                num_invoices_to_assign = 5
            if num_invoices_to_assign == 0:
                continue
            selected_invoices = random.sample(invoices, num_invoices_to_assign)
            claim.invoices = selected_invoices

            session.add(claim)

            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1} claims...")

        session.commit()
        print(
            f"Successfully seeded {MIN_NUM_CLAIM_FOR_EMPLOYEE_ID_1} claims for employee id = 1 {employee_1.name}"
        )
    except Exception as e:
        session.rollback()
        print(f"Error seeding claims for employee 1: {e}")
    finally:
        session.close()


def seed_claims():
    """Seed the database with fake claims"""

    try:
        for i in range(NUM_CLAIMS):
            selected_employee = Employee()
            invoices = []
            selected_invoices = List[Invoice]
            while not invoices:
                selected_employee, invoices = find_invoices_of_random_employee()

            status = random.choices(statuses, weights=[10, 60, 30], k=1)[0]
            claim = Claim(
                claim_number=f"CLM-{fake.unique.random_number(digits=8)}",
                employee_id=selected_employee.id,  # Use actual employee ID from DB
                claim_type=random.choice(claim_types),
                reason=fake.text(max_nb_chars=200),
                status=status,
                submitted_date=fake.date_between(start_date="-1y", end_date="today"),
                reviewed_date=fake.date_between(start_date="-6m", end_date="today")
                if random.choice([True, False])
                else None,
                resolution=fake.text(max_nb_chars=150)
                if random.choice([True, False])
                else None,
                is_anomaly=random.random() < 0.7 if status == "rejected" else False,
            )

            # Randomly assign 1-3 invoices to each claim using actual invoice IDs
            num_invoices_to_assign = random.randint(1, min(3, len(invoices)))
            if num_invoices_to_assign > 5:
                num_invoices_to_assign = 5
            if num_invoices_to_assign == 0:
                continue
            selected_invoices = random.sample(invoices, num_invoices_to_assign)
            claim.invoices = selected_invoices

            session.add(claim)

            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1} claims...")

        session.commit()
        print(
            f"Successfully seeded {NUM_CLAIMS} claims with actual employee and invoice relationships!"
        )

    except Exception as e:
        session.rollback()
        print(f"Error seeding claims: {e}")
    finally:
        session.close()


def show_help():
    """Show usage instructions"""
    print("Claim Seeder")
    print("=" * 50)
    print("Usage:")
    print(
        "  python claim_seeder.py --number 30        - Seed 30 number of claims (DEFAULT: 20)"
    )
    print("  python claim_seeder.py -n 30             - Shortcut for above")
    print("  python claim_seeder.py --help             - Show this help message")
    print("  python claim_seeder.py -h                 - Shortcut for above")
    print()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        seed_claims()
    elif len(sys.argv) == 2 and sys.argv[1] in ["--help", "-h"]:
        show_help()
    elif len(sys.argv) == 3 and sys.argv[1] in ["--number", "-n"]:
        try:
            NUM_CLAIMS = int(sys.argv[2])
            seed_claims_for_employee_id_1()
            seed_claims()
        except ValueError:
            print("Error: Please provide a valid number")
            show_help()
    else:
        print("Error: Invalid arguments")
        show_help()
