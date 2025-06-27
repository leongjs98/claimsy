import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.tables import Base, engine


def create_all_tables():
    """
    Creates all tables defined inheriting from Base in the database.
    """
    try:
        Base.metadata.create_all(engine)
        print("All tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    create_all_tables()
