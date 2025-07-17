from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
import uuid
from typing import List
from db.postgresql_setup import get_db
from db.tables import Claim as DBClaim
from db.tables import Invoice as DBInvoice
from db.schemas import ClaimSchema, InvoiceSchema, SubmitClaimRequest
from llm.reader import encode_image_file
from llm.setup import chain_extract_invoice_info, output_parser_invoice_json

router = APIRouter()

#TODO: link employee-claim.ts to employee/{employee_id}/claim/all
# connect two table claims + invoice
@router.get("/{employee_id}/claim/all", response_model=List[ClaimSchema])
def get_all_claims(employee_id: int, db: Session = Depends(get_db)):
    try:
        claims = db.query(DBClaim).filter(DBClaim.employee_id == employee_id).all()

        for claim in claims:
            claim.Items = db.query(DBInvoice).filter(DBInvoice.claim_id == claim.id).all()

        return claims
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve claims. {str(e)}",
        )

@router.post("/analyze/invoice")
async def analyze_invoice(
    files: List[UploadFile] = File(...),  # need to add more file(Multiplefile)):
):
    results = []

    for file in files:
        try:
            image_base64 = encode_image_file(file)

            response = chain_extract_invoice_info.invoke({
                "image": image_base64,
                "format_instructions": output_parser_invoice_json.get_format_instructions()
            })

            results.append(response)
        except Exception as e:
            results.append({"error": str(e)})
    return {"answers": results}

# sho - create endpoint for unsubmitted invoices
@router.get("/{employee_id}/invoice/unsubmitted", response_model=List[InvoiceSchema])
def get_unsubmitted_invoices(employee_id: int, db: Session = Depends(get_db)):
    try:
        # Example: invoices where claim_id is None (not submitted)
        invoices = db.query(DBInvoice).filter(
            DBInvoice.employee_id == employee_id,
            DBInvoice.claim_id.is_(None)  # or whatever logic marks as "unsubmitted"
        ).order_by(DBInvoice.invoice_date.desc()).all()
        return invoices
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve unsubmitted invoices. {str(e)}",
        )
# until here

# TODO: create router for /employee/claim/{id}/edit, (submit here = save)

# TODO: complete API /employee/{employee_id}/invoice/submit-into-claim
# input: multiple invoices.id
# output: claim
# page: /employee/claim/expenses
@router.post(
    "/{employee_id}/invoice/submit-into-claim", 
    response_model=ClaimSchema
)
def submit_invoices_into_claims(
    employee_id: int, 
    request: SubmitClaimRequest,
    db: Session = Depends(get_db)
):
    try:
        # 1. Validate that invoice_ids are provided
        if not request.invoice_ids:
            raise HTTPException(
                status_code=400, 
                detail="At least one invoice must be selected"
            )
        
        # 2. Fetch the selected invoices and validate them
        invoices = db.query(DBInvoice).filter(
            DBInvoice.id.in_(request.invoice_ids),
            DBInvoice.employee_id == employee_id,
            DBInvoice.claim_id.is_(None)  # Only invoices not already claimed
        ).all()
        
        # 3. Validate that all requested invoices exist and are available
        if len(invoices) != len(request.invoice_ids):
            raise HTTPException(
                status_code=400,
                detail="Some invoices are not found, don't belong to this employee, or are already claimed"
            )
        
        # 4. Calculate total claim amount
        # Assuming you have a way to calculate total amount per invoice
        # You might need to add this calculation based on item_services
        total_claim_amount = 0
        for invoice in invoices:
            # Calculate invoice total from item_services
            invoice_total = sum(
                item.quantity * item.unit_price 
                for item in invoice.item_services
            )
            total_claim_amount += invoice_total
        
        # 5. Generate unique claim number
        claim_number = f"CLM-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
        
        # 6. Create new claim
        new_claim = DBClaim(
            claim_number=claim_number,
            employee_id=employee_id,
            claim_type=request.claim_type,
            claim_amount=total_claim_amount,
            reason=request.reason,
            status="Pending",  # Initial status
            submitted_date=datetime.now(),
            created_at=int(datetime.now().timestamp()),
            updated_at=int(datetime.now().timestamp())
        )
        
        # 7. Save the claim to get the generated ID
        db.add(new_claim)
        db.flush()  # This will assign the ID without committing
        
        # 8. Update all selected invoices with the new claim_id
        db.query(DBInvoice).filter(
            DBInvoice.id.in_(request.invoice_ids)
        ).update(
            {
                "claim_id": new_claim.id,
                "updated_at": int(datetime.now().timestamp())
            },
            synchronize_session=False
        )
        
        # 9. Commit the transaction
        db.commit()
        db.refresh(new_claim)
        
        return new_claim
        
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{claim_id}/invoice/all", response_model=List[InvoiceSchema])
def get_invoices_details(
    claim_id: int, db: Session = Depends(get_db)
):
    try:
        # Show all invoices for specific invoices
        invoices = db.query(DBInvoice).filter(
            DBInvoice.claim_id == claim_id ).all()
        return invoices
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve invoices. {str(e)}",
        )
    
# TODO: complete API {employee_id}/invoice/{invoice_id}
# show invoice details in employee/claim/edit
@router.get("/{employee_id}/invoice/{invoice_id}", response_model=InvoiceSchema)
def get_invoice_details(
    employee_id: int, invoice_id: int, db: Session = Depends(get_db)
):
    return {}


