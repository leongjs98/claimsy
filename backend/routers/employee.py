from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy.orm import Session
from typing import List
from db.setup import get_db
from db.tables import Claim
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document
from pypdf import PdfReader
from io import BytesIO

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


@router.get("/")
def read_root():
    return {"message": "Hello World"}


@router.get("/claims", response_model=List[ClaimSchema])
def get_all_claims(db: Session = Depends(get_db)):
    return db.query(Claim).all()
