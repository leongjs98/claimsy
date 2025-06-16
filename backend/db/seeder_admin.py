from sqlalchemy.orm import sessionmaker
import bcrypt
from setup import engine
from tables import Admin

Session = sessionmaker(bind=engine)
db = Session()


def create_test_admin():
    try:
        password = "testtest"
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        existing_admin = (
            db.query(Admin)
            .filter((Admin.username == "test_admin") | (Admin.admin_id == "ADM001"))
            .first()
        )

        if existing_admin:
            print("Test admin already exists. Skipping creation.")
        else:
            new_admin = Admin(
                admin_id="ADM001", username="test_admin", password_hash=hashed_password
            )
            db.add(new_admin)
            db.commit()
            db.refresh(new_admin)
            print(f"Test admin '{new_admin.username}' created successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error creating test admin: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    create_test_admin()
