"""
Create random mock data of invoices
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from faker import Faker
import random
import json
from backend.db.tables import Employee, Invoice
from backend.db.postgresql_setup import session

NUM_INVOICES = 50  # Default value
MIN_NUM_INVOICES_FOR_EMPLOYEE_ID_1 = 20

fake = Faker()

categories = (
    "Supplies and Equipment",
    "Travel",
    "Meals & Entertaiment",
    "Accommodation",
    "Medical",
)


def create_invoice_data(i, employee_ids):
    """Create fake invoice data"""
    return {
        "invoice_id": i + 1,
        "invoice_number": f"INV-{fake.year()}-{fake.random_int(min=1000, max=9999)}",
        "employee_id": random.choice(employee_ids),
        "invoice_date": fake.date_between(start_date="-2y", end_date="today"),
        "category": fake.random_element(elements=categories),
        "merchant_name": fake.company(),
        "merchant_address": fake.address(),
        "items_services": json.dumps([
            {
                "item": fake.catch_phrase(),
                "quantity": fake.random_int(min=1, max=10),
                "unit_price": float(fake.random_int(min=10, max=500)),
            }
            for _ in range(fake.random_int(min=1, max=5))
        ]),
        "remark": fake.text(max_nb_chars=200)
        if fake.boolean(chance_of_getting_true=70)
        else None,
    }

def seed_invoices_for_employee_id_1():
    """Seed the database with invoice data"""
    try:
        invoices = []
        used_invoice_numbers = set()

        for i in range(MIN_NUM_INVOICES_FOR_EMPLOYEE_ID_1):
            while True:
                invoice_data = create_invoice_data(i, [1])

                # Ensure unique invoice number
                if invoice_data["invoice_number"] not in used_invoice_numbers:
                    used_invoice_numbers.add(invoice_data["invoice_number"])
                    break

            invoice = Invoice(**invoice_data)
            invoices.append(invoice)

            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1} invoices for employee id 1...")

        session.add_all(invoices)
        session.commit()

        print(f"Successfully seeded {MIN_NUM_INVOICES_FOR_EMPLOYEE_ID_1} invoices for employee id 1!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding invoices: {e}")
    finally:
        session.close()

def seed_invoices():
    """Seed the database with invoice data"""
    try:
        # Get existing employee IDs from database
        employee_ids = [emp.id for emp in session.query(Employee.id).all()]

        if not employee_ids:
            print("No employees found in database. Please seed employees first.")
            return

        print(f"Creating {NUM_INVOICES} invoices...")

        invoices = []
        used_invoice_numbers = set()

        for i in range(NUM_INVOICES):
            while True:
                invoice_data = create_invoice_data(i, employee_ids)

                # Ensure unique invoice number
                if invoice_data["invoice_number"] not in used_invoice_numbers:
                    used_invoice_numbers.add(invoice_data["invoice_number"])
                    break

            invoice = Invoice(**invoice_data)
            invoices.append(invoice)

            if (i + 1) % 10 == 0:
                print(f"Generated {i + 1} invoices...")

        session.add_all(invoices)
        session.commit()

        print(f"Successfully seeded {NUM_INVOICES} invoices!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding invoices: {e}")
    finally:
        session.close()


def show_help():
    """Show usage instructions"""
    print("Invoice Seeder")
    print("=" * 50)
    print("Usage:")
    print(
        "will seed at least 20 invoices for employee 1"
    )
    print(
        "  python invoice_seeder.py --number 30        - Seed 30 number of invoices (DEFAULT: 20)"
    )
    print("  python invoice_seeder.py -n 30             - Shortcut for above")
    print("  python invoice_seeder.py --help             - Show this help message")
    print("  python invoice_seeder.py -h                 - Shortcut for above")
    print()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        seed_invoices()
    elif len(sys.argv) == 2 and sys.argv[1] in ["--help", "-h"]:
        show_help()
    elif len(sys.argv) == 3 and sys.argv[1] in ["--number", "-n"]:
        try:
            NUM_INVOICES = int(sys.argv[2])
            seed_invoices()
            seed_invoices_for_employee_id_1()
        except ValueError:
            print("Error: Please provide a valid number")
            show_help()
    else:
        print("Error: Invalid arguments")
        show_help()
