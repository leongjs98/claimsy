from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Form
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from sqlalchemy.orm import Session
from typing import List
from db.setup import get_db
from db.tables import Claim
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document
from pypdf import PdfReader
from io import BytesIO
import base64
from typing import Annotated
from typing import Literal


router = APIRouter()

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    api_key=os.getenv("GEMINI_API_KEY")
)


def read_file(file_contents: BytesIO) -> str:
    reader = PdfReader(file_contents)
    text = ""
    for page in reader.pages:
        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        except Exception as e:
            print(f"Warning: Could not extract text from a page in the PDF: {e}")
            continue
    return text


@router.post("employee/claim/upload")
async def employee_claim_upload(file: UploadFile = File(...)):
    allowed_extensions = ["pdf", "png", "jpg"]
    if not file.filename.lower().endswith(allowed_extensions):
        # might need to alter the front end putting in text saying file must be in pdf, png or jpg format
        raise HTTPException(status_code=400, detail="File must be in a correct format")

    try:
        contents = await file.read()
        file_contents = BytesIO(contents)
        extracted_text = read_file(file_contents)

        if not extracted_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract any readable text from the PDF. It might be an image-only PDF, encrypted, or empty.",
            )

        doc = [Document(page_content=extracted_text)]

        summarization_prompt_template = """
        Please provide a concise and comprehensive summary of the following document.
        Focus on the main points, key information, and overall purpose.

        Document:
        "{text}"

        CONCISE SUMMARY:
        """
        prompt = PromptTemplate(
            template=summarization_prompt_template, input_variables=["text"]
        )

        summary_chain = load_summarize_chain(llm=llm, chain_type="stuff", prompt=prompt)

        summary_output = summary_chain.invoke({"input_documents": doc})

        return {"summary": summary_output["output_text"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


class ClaimSchema(BaseModel):
    id: int
    claim_number: str
    invoice_id: int
    employee_id: int
    claim_type: Optional[str] = None
    claim_amount: float
    reason: Optional[str] = None
    status: Optional[str] = None
    submitted_date: Optional[date] = None
    reviewed_date: Optional[date] = None
    resolution: Optional[str] = None

    class Config:
        orm_mode = True



load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that extract structured information from images like invoices"),
    ("human", [
        {"type": "text", "text": "{input}"},
        {
            "type": "image_url",
            "image_url": {
                "url": "data:image/jpg;base64,{image}",
                "detail": "low",
            },
        },
    ]),
])

chain = prompt | llm

def encode_image_file(file: UploadFile) -> str:
    return base64.b64encode(file.file.read()).decode("utf-8")

@router.post("/analyze/invoice")
async def analyze_invoice(files: List[UploadFile] = File(...)):  #need to add more file(Multiplefile)):
    results = []
    
    for file in files:
        try: 
            image_base64 = encode_image_file(file)

            response = chain.invoke({
                "image": image_base64,
                "format_instructions": output_parser.get_format_instructions()
            })

            results.append(response)
        except Exception as e:
            results.append({"error": str(e)})
    return {"answers": results}
    


class ItemRow(BaseModel):
    description: str = Field(description="Item or service description")
    quantity: int = Field(description="Quantity purchased")
    unit_price: float = Field(description="Price per unit")

class InvoiceInfo(BaseModel):
    category: Literal[
        "Gadget",
        "Travel Expenses",
        "Meals and Entertainment",
        "Accomodation",
        "Communication"
    ] = Field(description="Type of invoice")
    date: str = Field(description="Date of the invoice in YYYY-MM-DD format")
    merchant_name: str = Field(description="Name of the shop or service provider")
    merchant_address: str = Field(description="Address of the merchant")
    remark: str = Field(description="Any additional notes from the invoice")
    items: List[ItemRow] = Field(description="List of items or services purchased")

output_parser = JsonOutputParser(pydantic_object=InvoiceInfo)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            "You are an AI assistant that extracts structured invoice data from receipt images.

            Always return the result in the following JSON format:

            - category
            - date
            - merchant_name
            - merchant_address
            - remark
            - items: a list of item entries. If items are not found, return an empty list (`[]`)."

            """
        ),
        (
            "human", [
                {"type": "text", "text": "{format_instructions}"},
                {
                    "type":"image_url",
                    "image_url": {
                        "url": "data:image/jpg;base64,{image}",
                        "detail": "low",
                    },
                },
            ]),
    ])

chain = prompt | llm | output_parser


@router.get("/claims", response_model=List[ClaimSchema])
def get_all_claims(db: Session = Depends(get_db)):
    return db.query(Claim).all()


