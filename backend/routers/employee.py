from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.postgresql_setup import get_db
from db.tables import Claim as DBClaim
from db.schemas import ClaimSchema, InvoiceSchema
from llm.reader import encode_image_file
from llm.setup import chain_extract_invoice_info, output_parser_invoice_json


router = APIRouter()


@router.get("{employee_id}/claim/all", response_model=List[ClaimSchema])
def get_all_claims(employee_id: int, db: Session = Depends(get_db)):
    try:
        claims = db.query(DBClaim).filter(DBClaim.employee_id == employee_id).all()
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


# TODO: create router for /employee/claim/{id}/edit, (submit here = save)


# TODO: complete API /employee/{employee_id}/invoice/submit-into-claim
# input: multiple invoices.id
# output: claim
# page: /employee/claim/expenses
@router.post(
    "/employee/{employee_id}/invoice/submit-into-claim", response_model=ClaimSchema
)
def submit_invoices_into_claims(employee_id: int, db: Session = Depends(get_db)):
    return {}


# TODO: complete API {employee_id}/invoice/{invoice_id}
# show invoice details in employee/claim/edit
@router.get("{employee_id}/invoice/{invoice_id}", response_model=InvoiceSchema)
def get_invoice_details(
    employee_id: int, invoice_id: int, db: Session = Depends(get_db)
):
    return {}
