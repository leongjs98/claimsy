"""
Create random mock data of claims based on NUM_RECORDS
MUST RUN AFTER seeder_employee.py and seeder_invoice.py
Due to Foreign keys
"""

import os
import sys
from typing import List
import json
from datetime import datetime
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
            print(claim.claim_number, claim.invoices)

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
    """Seed the database with claims data from JSON file"""
    try:
        # Get existing employee IDs from database
        employee_ids = [emp.id for emp in session.query(Employee.id).all()]
        
        if not employee_ids:
            print("No employees found in database. Please seed employees first.")
            return

        # Load claims data from JSON file
        with open('./seeder/data/claims.json', 'r') as file:
            claims_data_list = json.load(file)
        
        print(f"Loading {len(claims_data_list)} claims from claims.json...")

        claims = []
        used_claim_numbers = set()
        skipped_count = 0

        for i, claim_data in enumerate(claims_data_list):
            try:
                # # Ensure unique claim number
                # if claim_data["claim_number"] in used_claim_numbers:
                #     print(f"Skipping duplicate claim number: {claim_data['claim_number']}")
                #     skipped_count += 1
                #     continue
                # 
                # used_claim_numbers.add(claim_data["claim_number"])
                
                # Validate employee_id exists
                if claim_data["employee_id"] not in employee_ids:
                    print(f"Skipping claim {claim_data['claim_number']}: employee_id {claim_data['employee_id']} not found")
                    skipped_count += 1
                    continue
                
                # Check if there are available invoices for this employee BEFORE creating the claim
                available_invoices = session.query(Invoice).filter(
                    Invoice.employee_id == claim_data["employee_id"],
                    Invoice.claim_id.is_(None)
                ).all()
                
                if not available_invoices:
                    print(f"Skipping claim {claim_data['claim_number']}: no available invoices for employee_id {claim_data['employee_id']}")
                    skipped_count += 1
                    continue
                
                # Convert date strings to date objects if needed
                if isinstance(claim_data.get("submitted_date"), str):
                    claim_data["submitted_date"] = datetime.strptime(
                        claim_data["submitted_date"], "%Y-%m-%d"
                    ).date()
                
                if claim_data.get("reviewed_date") and isinstance(claim_data["reviewed_date"], str):
                    claim_data["reviewed_date"] = datetime.strptime(
                        claim_data["reviewed_date"], "%Y-%m-%d"
                    ).date()

                # Create Claim object
                claim = Claim(**claim_data)
                claims.append(claim)

                if len(claims) % 10 == 0:
                    print(f"Processed {len(claims)} claims...")
                    
            except Exception as e:
                print(f"Error processing claim {i+1}: {e}")
                skipped_count += 1
                continue

        # Add all valid claims to session first
        if claims:
            session.add_all(claims)
            session.flush()  # Flush to get claim IDs without committing
            
            # Now assign random invoices to each claim
            claims_with_invoices = []
            for claim in claims:
                try:
                    # Get invoices with null claim_id for this employee
                    available_invoices = session.query(Invoice).filter(
                        Invoice.employee_id == claim.employee_id,
                        Invoice.claim_id.is_(None)
                    ).all()
                    
                    if available_invoices:
                        # Randomly select 1-3 invoices
                        num_invoices_to_assign = random.randint(1, min(3, len(available_invoices)))
                        selected_invoices = random.sample(available_invoices, num_invoices_to_assign)
                        
                        # Assign claim_id to selected invoices
                        for invoice in selected_invoices:
                            invoice.claim_id = claim.id
                            
                        claims_with_invoices.append(claim)
                        print(f"Assigned {num_invoices_to_assign} invoices to claim {claim.claim_number}")
                    else:
                        # Remove claim from session if no invoices available
                        session.expunge(claim)
                        print(f"Removed claim {claim.claim_number}: no invoices available")
                    
                except Exception as e:
                    print(f"Error assigning invoices to claim {claim.claim_number}: {e}")
                    # Remove claim from session if error occurs
                    session.expunge(claim)
                    continue
            
            session.commit()
            print(f"Successfully seeded {len(claims_with_invoices)} claims with invoices!")
            
            claims_without_invoices = len(claims) - len(claims_with_invoices)
            if claims_without_invoices > 0:
                print(f"Removed {claims_without_invoices} claims that had no invoices available.")
            
            if skipped_count > 0:
                print(f"Skipped {skipped_count} invalid records.")
        else:
            print("No valid claim records found to seed.")
        
    except FileNotFoundError:
        print("Error: claims.json file not found!")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
    except Exception as e:
        print(f"Error seeding claims: {e}")
        session.rollback()
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
            seed_claims()
        except ValueError:
            print("Error: Please provide a valid number")
            show_help()
    else:
        print("Error: Invalid arguments")
        show_help()
