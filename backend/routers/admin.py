from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session, joinedload
from db.postgresql_setup import get_db
from db.tables import Invoice as DBInvoice
from db.tables import Claim as DBClaim
from db.schemas import InvoiceSchema, ClaimSchema, EmployeeScheme


router = APIRouter()


@router.get("/claim/all", response_model=List[ClaimSchema])
def get_all_claims(db: Session = Depends(get_db)):
    """
    Show all claim made by every employee
    """
    try:
        claims = db.query(DBClaim).options(joinedload(DBClaim.employee)).all()
        return claims
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve claims. {str(e)}",
        )


@router.get("/invoice/all", response_model=List[InvoiceSchema])
async def list_invoices(db: Session = Depends(get_db)):
    """
    Show all invoices made by every employee
    """
    try:
        invoices = db.query(DBInvoice).order_by(DBInvoice.id.desc()).all()
        return [InvoiceSchema.model_validate(invoice) for invoice in invoices]
    except Exception as e:
        print(f"Error fetching invoices: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve invoices. {str(e)}",
        )


@router.get("/invoice/{invoice_id}", response_model=InvoiceSchema)
async def get_invoice_by_id(invoice_id: int, db: Session = Depends(get_db)):
    """
    Show the details of a invoice
    """
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


# TODO: output (output_parser) JSON for the fields in /admin/policy/edit (not save first)
# TODO: create /admin/policy/edit, (submit here = save)
@router.get("/policy")
async def get_policy_details():
    """
    Show the details of the policy
    """
    return {
        "validClaimCriteria": [
            "Must fall under eligible categories",
            "Medical, Supplies/Equipment, Travel, Meals/Entertainment, Accommodation",
            "Submitted within required timeframes (30 days general, 60 days medical)",
            "Include original receipts and completed expense forms",
            "Have proper business justification and manager approval",
            "Stay within spending limits (Medical: RM500, Meals: RM50/day travel, RM25/person business)",
            "Medical claims require medical certificates",
        ],
        "fraudulentClaimsIndicators": [
            "False or altered receipts and signatures",
            "Double claiming same expense",
            "Personal expenses claimed as business",
            "Deliberately inflated amounts",
            "Claims for non-existent expenses",
            "Fake medical certificates",
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


# TODO: complete API /claim/{claim_id}/details ---> DONE (Diana)
# for page /admin/claim/review/{claim_id}
# get all the invoices linkeed to the claim
@router.get("/claim/{claim_id}/details", response_model=ClaimSchema)
async def get_claim_by_id(claim_id: int, db: Session = Depends(get_db)):
    """
    Get claim by claim_id
    """
    try:
        claim = db.query(DBClaim).options(joinedload(DBClaim.invoices)).filter(DBClaim.id == claim_id).first()
        if claim is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Claim with ID {claim_id} not found",
            )
        return claim
    except Exception as e:
        print(f"Error fetching claim with ID {claim_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve invoice. {str(e)}",
        )


# for page /admin/claim/review/{claim_id}
# approved = True, set status approve
# approved = False, set status reject
# TODO: account for pending
# @router.post("/claim/{claim_id}/resolve/{status}", response_model=InvoiceSchema)
@router.post("/claim/{claim_id}/resolve/{approved}", response_model=ClaimSchema)
def approve_or_reject_claim( claim_id: int, approved: bool, db: Session = Depends(get_db)):
    """
    Approve or reject a claim.
    - approved = True: set status to 'approved'
    - approved = False: set status to 'rejected'
    """
    try:
        claim = db.query(DBClaim).filter(DBClaim.id == claim_id).first()
        if claim is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Claim with ID {claim_id} not found",
            )

        if approved:
            claim.status = "approved"
            print(f"Claim {claim_id} approved.")
        else:
            claim.status = "rejected"
            # claim.remark = request_body.remark # Update remark if provided (e.g., reason for rejection)
            print(f"Claim {claim_id} rejected.")

        db.add(claim)
        db.commit()
        db.refresh(claim)

        return claim 
    except Exception as e:
        print(f"Error resolving claim {claim_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not resolve claim. {str(e)}",
        )
