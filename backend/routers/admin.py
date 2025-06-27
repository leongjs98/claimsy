from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
from db.setup import get_db
from db.tables import Invoice as DBInvoice
from db.schemas import InvoiceSchema


router = APIRouter()


@router.get("/claim/details", response_model=List[InvoiceSchema])
async def list_invoices(db: Session = Depends(get_db)):
    try:
        invoices = db.query(DBInvoice).order_by(DBInvoice.id.desc()).all()
        return [InvoiceSchema.model_validate(invoice) for invoice in invoices]
    except Exception as e:
        print(f"Error fetching invoices: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve invoices. {str(e)}",
        )


@router.get("/invoice/details/{invoice_id}", response_model=InvoiceSchema)
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
