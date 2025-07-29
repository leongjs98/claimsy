"""
Create random mock data of invoices
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from faker import Faker
import random
import json
from backend.db.tables import Employee, Invoice
from backend.db.postgresql_setup import session
from backend.db.values import categories

NUM_INVOICES = 50  # Default value
MIN_NUM_INVOICES_FOR_EMPLOYEE_ID_1 = 50

fake = Faker()


def create_invoice_data(employee_ids):
    """Create fake invoice data"""
    date = fake.date_between(start_date="-2y", end_date="today")
    return {
        "invoice_number": f"INV-{date.year}-{fake.random_int(min=1000, max=9999)}-{fake.random_int(min=1000, max=9999)}",
        "employee_id": random.choice(employee_ids),
        "invoice_date": date,
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
                invoice_data = create_invoice_data([1])

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

        print(
            f"Successfully seeded {MIN_NUM_INVOICES_FOR_EMPLOYEE_ID_1} invoices for employee id 1!"
        )
    except Exception as e:
        session.rollback()
        print(f"Error seeding invoices: {e}")
    finally:
        session.close()


def seed_invoices():
    """Seed the database with invoice data from JSON file"""
    try:
        # Get existing employee IDs from database
        employee_ids = [emp.id for emp in session.query(Employee.id).all()]

        if not employee_ids:
            print("No employees found in database. Please seed employees first.")
            return

        # Load invoice data from JSON file
        with open('./seeder/data/invoices.json', 'r') as file:
            invoice_data_list = json.load(file)
        
        print(f"Loading {len(invoice_data_list)} invoices from invoices.json...")

        invoices = []
        used_invoice_numbers = set()
        skipped_count = 0

        for i, invoice_data in enumerate(invoice_data_list):
            try:
                # Ensure unique invoice number
                if invoice_data["invoice_number"] in used_invoice_numbers:
                    print(f"Skipping duplicate invoice number: {invoice_data['invoice_number']}")
                    skipped_count += 1
                    continue
                
                used_invoice_numbers.add(invoice_data["invoice_number"])
                
                # Validate employee_id exists
                if invoice_data["employee_id"] not in employee_ids:
                    print(f"Skipping invoice {invoice_data['invoice_number']}: employee_id {invoice_data['employee_id']} not found")
                    skipped_count += 1
                    continue
                
                # Convert invoice_date string to date object if needed
                if isinstance(invoice_data.get("invoice_date"), str):
                    invoice_data["invoice_date"] = datetime.strptime(
                        invoice_data["invoice_date"], "%Y-%m-%d"
                    ).date()
                
                # Create Invoice object
                invoice = Invoice(**invoice_data)
                invoices.append(invoice)

                if len(invoices) % 10 == 0:
                    print(f"Processed {len(invoices)} invoices...")
                    
            except Exception as e:
                print(f"Error processing invoice {i+1}: {e}")
                skipped_count += 1
                continue

        # Add all valid invoices to session
        if invoices:
            session.add_all(invoices)
            session.commit()
            print(f"Successfully seeded {len(invoices)} invoices!")
            if skipped_count > 0:
                print(f"Skipped {skipped_count} invalid records.")
        else:
            print("No valid invoice records found to seed.")
        
    except FileNotFoundError:
        print("Error: invoices.json file not found!")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
    except Exception as e:
        print(f"Error seeding invoices: {e}")
        session.rollback()
    finally:
        session.close()


def show_help():
    """Show usage instructions"""
    print("Invoice Seeder")
    print("=" * 50)
    print("Usage:")
    print("will seed at least 20 invoices for employee 1")
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
            # seed_invoices_for_employee_id_1()
        except ValueError:
            print("Error: Please provide a valid number")
            show_help()
    else:
        print("Error: Invalid arguments")
        show_help()
