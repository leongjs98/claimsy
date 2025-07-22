from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime
import json
import random
from typing import List
from db.postgresql_setup import get_db
from db.tables import Claim 
from db.tables import Invoice 
from db.schemas import ClaimSchema, InvoiceSchema, SubmitClaimRequest, ClaimStatus
from llm.reader import encode_image_file
from llm.setup import chain_extract_invoice_info, output_parser_invoice_json

router = APIRouter()

#TODO: link employee-claim.ts to employee/{employee_id}/claim/all
# connect two table claims + invoice
@router.get("/{employee_id}/claim/all", response_model=List[ClaimSchema])
def get_all_claims(employee_id: int, db: Session = Depends(get_db)):
    try:
        claims = db.query(Claim).filter(Claim.employee_id == employee_id).all()

        for claim in claims:
            claim.Items = db.query(Invoice).filter(Invoice.claim_id == claim.id).all()

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
        invoices = db.query(Invoice).filter(
            Invoice.employee_id == employee_id,
            Invoice.claim_id.is_(None)  # or whatever logic marks as "unsubmitted"
        ).order_by(Invoice.invoice_date.desc()).all()
        return invoices
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Could not retrieve unsubmitted invoices. {str(e)}",
        )
# until here

# TODO: create router for /employee/claim/{id}/edit, (submit here = save)

# aisya - employee/{employee_id}/invoice/submit-into-claim
@router.post("/{employee_id}/invoice/submit-into-claim", response_model=ClaimSchema)
def submit_invoices_into_claims(
    employee_id: int, 
    request: SubmitClaimRequest,
    db: Session = Depends(get_db)
):
    try:
        # Validate input
        if not request.invoice_ids:
            raise HTTPException(
                status_code=400, 
                detail="At least one invoice must be selected"
            )
        
        # Find and validate invoices
        invoices = db.query(Invoice).filter(
            Invoice.id.in_(request.invoice_ids),
            Invoice.employee_id == employee_id,
            Invoice.claim_id.is_(None)
        ).all()
        
        if len(invoices) != len(request.invoice_ids):
            raise HTTPException(
                status_code=400,
                detail="Some invoices are not found, don't belong to this employee, or are already claimed"
            )
        
        # Calculate total claim amount
        total_claim_amount = Decimal('0.00')
        
        for invoice in invoices:
            items_services = invoice.items_services
            
            # Parse JSON string if needed
            if isinstance(items_services, str):
                try:
                    items_services = json.loads(items_services)
                except json.JSONDecodeError:
                    continue
            
            # Calculate invoice total
            if items_services and isinstance(items_services, list):
                for item in items_services:
                    if isinstance(item, dict):
                        quantity = item.get('quantity', 0)
                        unit_price = item.get('unit_price', 0)
                        total_claim_amount += Decimal(str(quantity)) * Decimal(str(unit_price))
        
        # Generate claim number
        random_number = f"{random.randint(10000000, 99999999)}"
        claim_number = f"CLM-{random_number}"
        
        # Create new claim
        current_datetime = datetime.now()
        
        new_claim = Claim(
            claim_number=claim_number,
            employee_id=employee_id,
            claim_type=request.claim_type,
            claim_amount=total_claim_amount,
            reason=request.reason,
            status="pending",
            submitted_date=current_datetime.date(),
            created_at=current_datetime,
            updated_at=current_datetime
        )
        
        # Save claim and update invoices
        db.add(new_claim)
        db.flush()
        
        db.query(Invoice).filter(
            Invoice.id.in_(request.invoice_ids)
        ).update({"claim_id": new_claim.id, "updated_at": current_datetime})
        
        db.commit()
        db.refresh(new_claim)
        
        return new_claim
        
    except HTTPException:
        db.rollback()
        raise
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{claim_id}/invoice/all", response_model=List[InvoiceSchema])
def get_invoices_details(
    claim_id: int, db: Session = Depends(get_db)
):
    try:
        # Show all invoices for specific invoices
        invoices = db.query(Invoice).filter(
            Invoice.claim_id == claim_id ).all()
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


