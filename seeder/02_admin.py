"""
Create a single admin for testing
credentials at admin_username, admin_password
"""

import hashlib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.postgresql_setup import session
from backend.db.tables import Admin


ADMIN_USERNAME = "test_admin"
ADMIN_PASSWORD = "testtest"


def create_test_admin():
    try:
        password = ADMIN_PASSWORD
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        existing_admin = (
            session.query(Admin)
            .filter((Admin.username == ADMIN_USERNAME) | (Admin.admin_id == "ADM001"))
            .first()
        )

        if existing_admin:
            print("Test admin already exists. Skipping creation.")
        else:
            new_admin = Admin(
                admin_id="ADM001",
                username=ADMIN_USERNAME,
                password_hash=hashed_password,
            )
            session.add(new_admin)
            session.commit()
            session.refresh(new_admin)
            print(f"Test admin '{new_admin.username}' created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error creating test admin: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    create_test_admin()
