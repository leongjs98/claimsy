from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field
from db.setup import Session
from db.tables import Invoice as DBInvoice


# Pydantic model for individual item/service within items_services JSON
class ItemService(BaseModel):
    description: str
    quantity: int
    price: float = Field(..., alias="unit_price")
    total: float


# Pydantic model for the Invoice (response/request body)
class Invoice(BaseModel):
    id: Optional[int] = Field(None, alias="invoice_id")
    invoice_number: str
    invoice_date: date
    created_at: datetime
    updated_at: datetime
    category: str
    merchant_name: str
    merchant_address: str
    items_services: List[ItemService]
    remark: Optional[str]

    class Config:
        from_attributes = True
        populate_by_name = True


# Dependency to get the database session for each request
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/claim/details", response_model=List[Invoice])
async def list_invoices(db: Session = Depends(get_db)):
    try:
        invoices = db.query(DBInvoice).order_by(DBInvoice.id.desc()).all()
        return invoices
    except Exception as e:
        print(f"Error fetching invoices: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve invoices. {str(e)}",
        )


@router.get("/claim/details/{invoice_id}", response_model=Invoice)
async def get_invoice_by_id(invoice_id: int, db: Session = Depends(get_db)):
    try:
        invoice = db.query(DBInvoice).filter(DBInvoice.id == invoice_id).first()
        if invoice is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Invoice with ID {invoice_id} not found",
            )
        return invoice
    except Exception as e:
        print(f"Error fetching invoice with ID {invoice_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve invoice. {str(e)}",
        )


@router.get("/policy")
async def get_policy_details():
    return {
        "claim_eligibility_criteria": [
            "Conditions under which a claim is considered valid.",
            "Timeframe has changed",
        ],
        "claim_approval_limitations": [
            {
                "title": "Claim Approval & Limitations",
                "points": [
                    "Criteria for approval or rejection.",
                    "Forms of compensation (e.g., payment, replacement, repair).",
                    "Settlement process (e.g., bank transfer, in-store credit).",
                ],
            }
        ],
        "claim_denial": [
            {
                "title": "Claim Denial",
                "points": [
                    "Grounds for denial (e.g., lack of documentation, excluded events).",
                    "Right to appeal or request re-evaluation.",
                    "Rejection communication process.",
                ],
            }
        ],
    }
