from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.postgresql_setup import get_db
from db.tables import Claim as DBClaim
from db.schemas import ClaimSchema, InvoiceSchema
from llm.reader import encode_image_file
from llm.setup import chain_extract_invoice_info, output_parser_invoice_json
from db.tables import Invoice




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



@router.post("/employee/invoice/save", response_model=InvoiceSchema)
async def save_invoice(
    invoice: InvoiceSchema,
    db: Session = Depends(get_db)
):
    try:
        data = invoice.model_dump(by_alias=True)
        print("💡 Received data:", data)

        existing_invoice = db.query(Invoice).filter_by(invoice_number=data["invoiceNumber"]).first()
        if existing_invoice:
            return {"error": f"Invoice number {data['invoiceNumber']} already exists."}

        new_invoice = Invoice(
            invoice_id=data["invoiceId"],
            invoice_number=data["invoiceNumber"],
            claim_id=data["claimId"],
            employee_id=data["employeeId"],
            invoice_date=data["invoiceDate"],
            category=data["category"],
            merchant_name=data["merchantName"],
            merchant_address=data["merchantAddress"],
            items_services=data["itemsServices"],  # already list of dicts
            remark=data["remark"]
        )

        db.add(new_invoice)
        db.commit()
        db.refresh(new_invoice)

        return invoice  # returning Pydantic object

    except Exception as e:
        db.rollback()
        import traceback
        traceback.print_exc()
        return {"error": str(e)}



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
#page ni dekat my claims lepastu filter by claim_id
@router.get("{employee_id}/invoice/{invoice_id}", response_model=InvoiceSchema)
def get_invoice_details(
    employee_id: int, invoice_id: int, db: Session = Depends(get_db)
):
    return {}
