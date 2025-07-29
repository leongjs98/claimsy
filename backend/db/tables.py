"""
PostgreSQL Table Schemas of Claimsy
"""

from typing import List, Dict, Any
from sqlalchemy import (
    DECIMAL,
    JSON,
    Date,
    ForeignKey,
    Integer,
    Text,
    Column,
    String,
    Boolean,
)
from .postgresql_setup import TableBase, Base
from sqlalchemy.orm import relationship


class Admin(TableBase):
    __tablename__ = "admins"

    admin_id = Column(String(20), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Admin(id={self.id}, admin_id='{self.admin_id}', username='{self.username}')>"


class Employee(TableBase, Base):
    __tablename__ = "employees"

    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(20))
    department = Column(String(50))
    job_title = Column(String(50))
    hire_date = Column(Date)
    salary = Column(DECIMAL(10, 2))

    invoices = relationship(
        "Invoice",
        back_populates="employee",
        cascade="all, delete-orphan",
    )
    claims = relationship(
        "Claim",
        back_populates="employee",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Employee(employee_id='{self.employee_id}', name='{self.name}')>"


class Invoice(TableBase, Base):
    __tablename__ = "invoices"
    invoice_number = Column(String(50), unique=True, nullable=False)
    claim_id = Column(Integer, ForeignKey("claims.id"), nullable=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    invoice_date = Column(Date, nullable=False)
    category = Column(String(100))
    merchant_name = Column(String(255))
    merchant_address = Column(String(255))
    items_services = Column(JSON)
    remark = Column(Text)

    employee = relationship("Employee", back_populates="invoices")
    claim = relationship("Claim", back_populates="invoices")

    @property
    def items(self) -> List[Dict[str, Any]]:
        return self.items_services or []

    @items.setter
    def items(self, value: List[Dict[str, Any]]):
        self.items_services = value

    def __repr__(self):
        return f"<Invoice(invoice_number='{self.invoice_number}', merchant_name='{self.merchant_name}')>"


class Claim(TableBase, Base):
    __tablename__ = "claims"

    claim_number = Column(String(50), unique=True, nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    claim_type = Column(String(50))
    reason = Column(Text)
    status = Column(String(20), default="pending")
    submitted_date = Column(Date)
    reviewed_date = Column(Date)
    resolution = Column(Text)
    is_anomaly = Column(Boolean, default=False)
    anomalyReason = Column(Text, nullable=False)

    employee = relationship(
        "Employee",
        back_populates="claims",
    )
    invoices = relationship(
        "Invoice", back_populates="claim", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Claim(claim_number='{self.claim_number}', status='{self.status}')>"
