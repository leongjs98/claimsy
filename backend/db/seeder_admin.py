"""
Create a single admin for testing
credentials at admin_username, admin_password
"""

import hashlib
from setup import session
from tables import Admin

admin_username = "test_admin"
admin_password = "testtest"

def create_test_admin():
    try:
        password = admin_password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        existing_admin = (
            session.query(Admin)
            .filter((Admin.username == admin_username) | (Admin.admin_id == "ADM001"))
            .first()
        )

        if existing_admin:
            print("Test admin already exists. Skipping creation.")
        else:
            new_admin = Admin(
                admin_id="ADM001",
                username=admin_username,
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
