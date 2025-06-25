from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get("/policy")
async def get_policy_details():
    return {
        "claim_eligibility_criteria": [
            "Conditions under which a claim is considered valid.",
            "Timeframe has changed"
        ],
        "claim_approval_limitations": [
            {
                "title": "Claim Approval & Limitations",
                "points": [
                    "Criteria for approval or rejection.",
                    "Forms of compensation (e.g., payment, replacement, repair).",
                    "Settlement process (e.g., bank transfer, in-store credit)."
                ]
            }
        ], 
        "claim_denial": [
            {
                "title": "Claim Denial",
                "points": [
                    "Grounds for denial (e.g., lack of documentation, excluded events).",
                    "Right to appeal or request re-evaluation.",
                    "Rejection communication process."
                ]
            }
        ]
    }
