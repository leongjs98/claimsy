"""
Return list of Flight and Hotels Offers based on searching criteria.

Get exchange rate to convert back into MYR

Not doing transport search
"""

import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor, tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from serpapi import GoogleSearch

load_dotenv()


# https://serpapi.com/google-flights-api
@tool
def get_flights(
    departure_id: str,
    arrival_id: str,
    outbound_date: str,
    return_date: str,
    currency: str,
    travel_class: int,
    adults: int,
    max_price: int,
):
    """
    Tool: Search Flights

    Description: Search for round-trip flights between two destinations with specified criteria and budget constraints.

    Parameters (All Required):

    - departure_id (string, required):
      * Airport or city code for departure location
      * Use IATA 3-letter airport codes (e.g., 'LAX', 'JFK', 'LHR')
      * Or city codes (e.g., 'NYC', 'LON', 'PAR')

    - arrival_id (string, required):
      * Airport or city code for destination location
      * Use IATA 3-letter airport codes (e.g., 'CDG', 'NRT', 'SYD')
      * Or city codes (e.g., 'TYO', 'SIN', 'BKK')

    - outbound_date (string, required):
      * Departure date in YYYY-MM-DD format
      * Example: '2024-03-15'
      * Must be a future date

    - return_date (string, required):
      * Return date in YYYY-MM-DD format
      * Example: '2024-03-22'
      * Must be after outbound_date

    - currency (string, required):
      * Price currency code (3-letter ISO 4217 format)
      * Examples: 'USD', 'EUR', 'GBP', 'JPY', 'MYR', 'CAD', 'AUD'
      * All prices will be displayed in this currency

    - travel_class (integer, required):
      * 1 = Economy (most affordable, standard service)
      * 2 = Premium Economy (extra legroom, enhanced service)
      * 3 = Business (lie-flat seats, premium dining, lounge access)
      * 4 = First (luxury suites, personalized service, finest amenities)

    - adults (integer, required):
      * Number of adult passengers (18+ years)
      * Minimum: 1, Maximum: typically 9
      * Example: 2

    - max_price (integer, required):
      * Maximum budget per person in specified currency
      * Example: 1500 (for $1,500 USD per person)
      * Only flights within this budget will be returned

    Usage Examples:
    - Economy flight from NYC to London:
      departure_id='JFK', arrival_id='LHR', outbound_date='2024-04-10', return_date='2024-04-17', currency='USD', travel_class=1, adults=2, max_price=800

    - Business class from Tokyo to Singapore:
      departure_id='NRT', arrival_id='SIN', outbound_date='2024-05-20', return_date='2024-05-27', currency='JPY', travel_class=3, adults=1, max_price=300000

    Note: Prices are subject to availability and may change. Book quickly for best rates.
    """
    serp_api_params = {
        "hl": "en",
        "gl": "my",
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "engine": "google_flights",
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": currency,
        "travel_class": travel_class,
        "adults": adults,
        "max_price": max_price,
    }

    try:
        search = GoogleSearch(serp_api_params)
        results = search.get_dict()
        return results
    except Exception as e:
        return f"Error getting flights: {str(e)}"


# https://serpapi.com/google-hotels-api
@tool
def get_hotels(
    query: str,
    check_in_date: str,
    check_out_date: str,
    currency: str,
    adults: int,
    max_price: int,
    hotel_class: str,
):
    """
    Tool: Search Hotels

    **Required Parameters:**
    - `query`: The search location or hotel description (e.g., "Singapore Hotel Near Changi Airport", "Bali Resorts", "Hotels in Paris")
    - `check_in_date`: Check-in date in YYYY-MM-DD format (e.g., "2025-07-22"), must be future date
    - `check_out_date`: Check-out date in YYYY-MM-DD format (e.g., "2025-07-23"), must be after check_in_date
    - `currency`: 3-letter ISO currency code for pricing (e.g., "USD", "EUR", "GBP", "JPY", "MYR", "CAD", "AUD")

    **Optional Parameters:**
    - `adults`: Number of adult guests (defaults to 2 if not specified)
    - `max_price`: Maximum price limit for filtering results
    - `hotel_class`: Hotel star rating filter. Options:
      - Single class: "2", "3", "4", or "5"
      - Multiple classes: "2,3,4" (comma-separated)

    **Instructions:**
    1. Extract the location/hotel type from the user's request for the `query` parameter
    2. If dates are not provided, ask the user for check-in and check-out dates
    3. If currency is not specified, default to "USD"
    4. If the user mentions budget constraints, use the `max_price` parameter
    5. If the user specifies hotel quality preferences, use the `hotel_class` parameter
    6. Always ensure check-out date is after check-in date

    **Example Usage:**
    For a request like "Find me a 4-star hotel in Tokyo for 2 adults from March 15-18, 2025, budget under $200, in USD":
    - query: "Tokyo hotels"
    - check_in_date: "2025-03-15"
    - check_out_date: "2025-03-18"
    - adults: 1
    - currency: "MYR"
    - max_price: 200
    - hotel_class: "4"
    """
    serp_api_params = {
        "hl": "en",
        "gl": "my",
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "engine": "google_hotels",
        "q": query,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "currency": currency,
        "adults": adults,
        "max_price": max_price,
        "hotel_class": hotel_class,
    }

    try:
        search = GoogleSearch(serp_api_params)
        results = search.get_dict()
        return results
    except Exception as e:
        return f"Error getting flights: {str(e)}"


# @tool
# def get_flight_offers(symbols: str, base: str = "MYR", date: str = "latest") -> str:
#     """
#     """
#     try:
#         api = f"""
#         curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
#              -H "Content-Type: application/x-www-form-urlencoded" \
#              -d "grant_type=client_credentials&client_id={AMADEUS_API_KEY}&client_secret={AMADEUS_API_SECRET}"
#         """
#         response = requests.get(api)
#         result = response.json()
#         return result
#     except Exception as e:
#         return f"Error: {str(e)}"
