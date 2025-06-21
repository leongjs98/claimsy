from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy.orm import Session
from typing import List

from db.setup import get_db
from db.tables import Claim

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

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello World"}

@router.get("/claims", response_model=List[ClaimSchema])
def get_all_claims(db: Session = Depends(get_db)):
    return db.query(Claim).all()