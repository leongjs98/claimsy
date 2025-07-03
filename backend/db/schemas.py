import json
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field, field_validator
from decimal import Decimal
from enum import Enum
from datetime import datetime

class ItemService(BaseModel):
    item: str
    quantity: int
    unit_price: float

class InvoiceSchema(BaseModel):
    id: Optional[int] = None
    invoice_id: int = Field(alias="invoiceId")
    invoice_number: str = Field(alias="invoiceNumber")
    claim_id: Optional[int] = Field(alias="claimId", default=None)
    employee_id: int = Field(alias="employeeId")
    invoice_date: date = Field(alias="invoiceDate")
    category: Optional[str] = None
    merchant_name: Optional[str] = Field(alias="merchantName", default=None)
    merchant_address: Optional[str] = Field(alias="merchantAddress", default=None)
    items_services: List[ItemService] = Field(alias="itemsServices")
    remark: Optional[str] = None

    @field_validator('items_services', mode='before')
    @classmethod
    def parse_items_services(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format for items_services")
        return v

    class Config:
        from_attributes = True
        populate_by_name = True

class ClaimStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class ClaimSchema(BaseModel):
    id: int
    claim_number: str
    employee_id: int
    claim_type: Optional[str] = None
    claim_amount: Optional[Decimal] = None
    reason: Optional[str] = None
    status: ClaimStatus = ClaimStatus.PENDING
    submitted_date: Optional[date] = None
    reviewed_date: Optional[date] = None
    resolution: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    invoices: List[InvoiceSchema] = [] 
    
    class Config:
        from_attributes = True
        json_encoders = {
            Decimal: float
        }