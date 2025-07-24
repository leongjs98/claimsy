from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional, Literal
from db.postgresql_setup import get_db
from db.tables import Claim as DBClaim
from db.schemas import ClaimSchema, InvoiceSchema, ItemService
from llm.reader import encode_image_file
from llm.setup import chain_extract_invoice_info, output_parser_invoice_json
from db.tables import Invoice
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
import logging
import os, json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool



import requests
import re
from datetime import datetime

load_dotenv()


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


@router.post("/employee/invoice/save")
async def save_invoice(invoice: InvoiceSchema, db: Session = Depends(get_db)):
    try:
        data = invoice.model_dump(by_alias=True)
        print("💡 Received data:", data)

        # Check for duplicate invoice number
        existing_invoice = db.query(Invoice).filter_by(invoice_number=data["invoiceNumber"]).first()
        if existing_invoice:
            raise HTTPException(status_code=400, detail=f"Invoice number {data['invoiceNumber']} already exists.")

        # Create invoice with embedded JSON items
        new_invoice = Invoice(
            invoice_number=data["invoiceNumber"],
            claim_id=data.get("claimId"),
            employee_id=data["employeeId"],
            invoice_date=data["invoiceDate"],
            category=data.get("category"),
            merchant_name=data.get("merchantName"),
            merchant_address=data.get("merchantAddress"),
            items_services=data.get("itemsServices"),  # this is JSON
            remark=data.get("remark")
        )

        db.add(new_invoice)
        db.commit()
        db.refresh(new_invoice)
        return new_invoice


    except Exception as e:
        db.rollback()
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# TODO: create router for /employee/claim/{id}/edit, (submit here = save)

# TODO: complete API /employee/{employee_id}/invoice/submit-into-claim
# input: multiple invoices.id
# output: claim
# page: /employee/claim/expenses
        
class ChatMessage(BaseModel):
            role: Literal["user", "assistant"]
            content: str
            
class ChatRequest(BaseModel):
            question: Optional[str] = Field(default="", description="Latest user message")
            history: List[ChatMessage] = Field(default=[])
@router.post("/employee/ask-claimsy/smart-suggest/travel-transport")
async def travel_transport(request: ChatRequest):
    try:
        question = request.question.strip() if request.question else ""
        if not question:
            return {"answer": "Please describe your travel plan, such as date, origin, and destination."}

        # Initialize LLM
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain.agents import create_tool_calling_agent, AgentExecutor
        from langchain.tools import tool
        from langchain_core.prompts import ChatPromptTemplate
        import re
        from datetime import datetime
        
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=GEMINI_API_KEY)

        def extract_travel_details(query: str):
            """Extract travel details from user query"""
            details = {
                "departure_id": None,
                "arrival_id": None,
                "outbound_date": None,
                "return_date": None,
                "location": None
            }
            
            query_lower = query.lower()
            
            # Airport code mapping
            airport_mapping = {
                "kuala lumpur": "KUL",
                "kl": "KUL", 
                "penang": "PEN",
                "georgetown": "PEN",
                "london": "LHR",
                "singapore": "SIN",
                "bangkok": "BKK",
                "jakarta": "CGK",
                "bali": "DPS",
                "phuket": "HKT",
                "ho chi minh": "SGN",
                "hanoi": "HAN"
            }
            
            # Extract departure and arrival locations
            from_to_pattern = r"from\s+([^,\n]+?)\s+to\s+([^,\n.]+)"
            match = re.search(from_to_pattern, query_lower)
            
            if match:
                departure_city = match.group(1).strip()
                arrival_city = match.group(2).strip()
                
                # Map to airport codes
                for city, code in airport_mapping.items():
                    if city in departure_city:
                        details["departure_id"] = code
                    if city in arrival_city:
                        details["arrival_id"] = code
                        details["location"] = arrival_city.title()
            
            # Extract dates
            month_mapping = {
                "january": "01", "february": "02", "march": "03", "april": "04",
                "may": "05", "june": "06", "july": "07", "august": "08", 
                "september": "09", "october": "10", "november": "11", "december": "12"
            }
            
            # Pattern for "24th July 2025" or "24 July 2025"
            date_pattern = r"(\d{1,2})(?:st|nd|rd|th)?\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{4})"
            matches = re.findall(date_pattern, query_lower)
            
            if matches:
                day, month, year = matches[0]
                month_num = month_mapping.get(month, "01")
                details["outbound_date"] = f"{year}-{month_num}-{day.zfill(2)}"
                
                # Look for return date "to 26 July"
                to_pattern = r"to\s+(\d{1,2})(?:st|nd|rd|th)?\s+" + month
                to_match = re.search(to_pattern, query_lower)
                if to_match:
                    return_day = to_match.group(1)
                    details["return_date"] = f"{year}-{month_num}-{return_day.zfill(2)}"
            
            # Alternative: look for date ranges like "24-26 July"
            range_pattern = r"(\d{1,2})\s*(?:to|-)\s*(\d{1,2})\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{4})"
            range_match = re.search(range_pattern, query_lower)
            if range_match:
                start_day, end_day, month, year = range_match.groups()
                month_num = month_mapping.get(month, "01")
                details["outbound_date"] = f"{year}-{month_num}-{start_day.zfill(2)}"
                details["return_date"] = f"{year}-{month_num}-{end_day.zfill(2)}"
            
            return details

        @tool
        def search_flights(query: str) -> str:
            """Search for flights using SerpAPI Google Flights with user input"""
            try:
                # Extract details from the user query
                details = extract_travel_details(query)
                
                # Use extracted values or defaults
                departure_id = details["departure_id"] or "KUL"
                arrival_id = details["arrival_id"] or "PEN"
                outbound_date = details["outbound_date"] or "2025-07-24"
                return_date = details["return_date"] or "2025-07-26"
                
                url = "https://serpapi.com/search"
                params = {
                    "engine": "google_flights",
                    "departure_id": departure_id,
                    "arrival_id": arrival_id,
                    "outbound_date": outbound_date,
                    "return_date": return_date,
                    "currency": "MYR",
                    "gl": "my",
                    "hl": "en",
                    "api_key": os.getenv("SERPAPI_API_KEY")
                }
                
                response = requests.get(url, params=params, timeout=30)
                data = response.json()
                
                flights_data = []
                
                # Check for different response structures
                if "best_flights" in data and data["best_flights"]:
                    for flight in data["best_flights"][:3]:
                        flight_info = {
                            "type": "best_flight",
                            "airline": flight.get("flights", [{}])[0].get("airline", "N/A"),
                            "price": flight.get("price", "N/A"),
                            "duration": flight.get("total_duration", "N/A"),
                            "departure_time": flight.get("flights", [{}])[0].get("departure_airport", {}).get("time", "N/A"),
                            "arrival_time": flight.get("flights", [{}])[0].get("arrival_airport", {}).get("time", "N/A")
                        }
                        flights_data.append(flight_info)
                
                elif "other_flights" in data and data["other_flights"]:
                    for flight in data["other_flights"][:3]:
                        flight_info = {
                            "type": "other_flight", 
                            "airline": flight.get("flights", [{}])[0].get("airline", "N/A"),
                            "price": flight.get("price", "N/A"),
                            "duration": flight.get("total_duration", "N/A"),
                            "departure_time": flight.get("flights", [{}])[0].get("departure_airport", {}).get("time", "N/A"),
                            "arrival_time": flight.get("flights", [{}])[0].get("arrival_airport", {}).get("time", "N/A")
                        }
                        flights_data.append(flight_info)
                
                if flights_data:
                    return json.dumps({
                        "search_params": {
                            "from": departure_id,
                            "to": arrival_id,
                            "departure": outbound_date,
                            "return": return_date
                        },
                        "flights_found": len(flights_data),
                        "flights": flights_data
                    }, indent=2)
                else:
                    return json.dumps({
                        "search_params": {
                            "from": departure_id,
                            "to": arrival_id,
                            "departure": outbound_date,
                            "return": return_date
                        },
                        "error": "No flights found for these dates",
                        "suggestion": "Try different dates or check if the route is available"
                    })
                    
            except Exception as e:
                return json.dumps({"error": f"Flight search failed: {str(e)}"})

        @tool  
        def search_hotels(query: str) -> str:
            """Search for hotels using SerpAPI Google Hotels with user input"""
            try:
                # Extract details from the user query
                details = extract_travel_details(query)
                
                # Use extracted values or defaults
                location = details["location"] or "Georgetown Penang"
                check_in_date = details["outbound_date"] or "2025-07-24"
                check_out_date = details["return_date"] or "2025-07-26"
                
                url = "https://serpapi.com/search"
                params = {
                    "engine": "google_hotels",
                    "q": f"{location} hotels",
                    "check_in_date": check_in_date,
                    "check_out_date": check_out_date,
                    "adults": 1,
                    "currency": "MYR",
                    "gl": "my", 
                    "hl": "en",
                    "api_key": os.getenv("SERPAPI_API_KEY")
                }
                
                response = requests.get(url, params=params, timeout=30)
                data = response.json()
                
                if "properties" in data and data["properties"]:
                    hotels = []
                    for hotel in data["properties"][:3]:
                        hotels.append({
                            "name": hotel.get("name", "N/A"),
                            "price": hotel.get("rate_per_night", {}).get("lowest", "N/A"),
                            "rating": hotel.get("overall_rating", "N/A"),
                            "location": hotel.get("neighborhood", "N/A"),
                            "amenities": hotel.get("amenities", [])[:3]
                        })
                    return json.dumps({
                        "search_params": {
                            "location": location,
                            "check_in": check_in_date,
                            "check_out": check_out_date
                        },
                        "hotels": hotels
                    }, indent=2)
                else:
                    return json.dumps({
                        "search_params": {
                            "location": location,
                            "check_in": check_in_date,
                            "check_out": check_out_date
                        },
                        "error": "No hotels found"
                    })
                    
            except Exception as e:
                return json.dumps({"error": f"Hotel search failed: {str(e)}"})

        # Create agent with tools
        tools = [search_flights, search_hotels]
        
        agent_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a travel agent with access to real-time flight and hotel search tools. 
            
            When users ask about travel:
            1. ALWAYS use the search_flights tool first to get real flight data
            2. ALWAYS use the search_hotels tool to get real hotel data
            3. Present the actual search results with real prices and details
            4. If no results found, suggest alternative dates or routes
            5. Be helpful and provide specific recommendations based on the real data
            
            Format your response professionally with the actual search results."""),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}")
        ])

        agent = create_tool_calling_agent(llm, tools, agent_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        # Execute the agent with the user's question
        result = agent_executor.invoke({"input": question})
        
        return {"answer": result["output"]}

    except Exception as e:
        logging.exception("Error in travel_transport")
        return {"answer": f"Error searching travel options: {str(e)}"}
    
@router.post("/test")
async def test_endpoint(request: ChatRequest):
    return {"question": request.question, "history": request.history}


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