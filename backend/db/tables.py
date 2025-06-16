from sqlalchemy import DECIMAL, JSON, Date, ForeignKey, Text, Column, Integer, String
from setup import TableBase, Base, engine


class Invoice(TableBase):
    __tablename__ = "invoices"

    invoice_number = Column(String(50), nullable=False)
    invoice_date = Column(Date, nullable=False)
    category = Column(String(100))
    merchant_name = Column(String(255))
    merchant_address = Column(String(255))
    items_services = Column(JSON)
    remark = Column(Text)

    def __repr__(self):
        return f"<Invoice(id={self.id}, invoice_number='{self.invoice_number}')>"


class Claim(TableBase):
    __tablename__ = "claims"

    claim_number = Column(String(50), nullable=False)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    claim_type = Column(String(50))
    claim_amount = Column(DECIMAL(10, 2), nullable=False)
    reason = Column(Text)
    status = Column(String(20))
    submitted_date = Column(Date)
    reviewed_date = Column(Date)
    resolution = Column(Text)

    def __repr__(self):
        return f"<Claim(id={self.id}, claim_number='{self.claim_number}')>"


class Employee(TableBase):
    __tablename__ = "employees"

    employee_id = Column(String(20), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(20))
    department = Column(String(50))
    job_title = Column(String(50))
    hire_date = Column(Date)
    salary = Column(DECIMAL(10, 2))

    def __repr__(self):
        return f"<Employee(id={self.id}, employee_id='{self.employee_id}', name='{self.name}')>"


class Admin(TableBase):
    __tablename__ = "admins"

    admin_id = Column(String(20), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Admin(id={self.id}, admin_id='{self.admin_id}', username='{self.username}')>"


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
