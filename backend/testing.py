import os
from amadeus import Client, Location, ResponseError
from dotenv import load_dotenv

load_dotenv()

amadeus = Client(
    client_id=os.getenv('AMADEUS_API_KEY'),
    client_secret=os.getenv('AMADEUS_API_SECRET')
)

try:
    # response = amadeus.shopping.flight_offers_search.get(
    #     originLocationCode='SIN',
    #     destinationLocationCode='BKK',
    #     departureDate='2025-08-15',
    #     returnDate='2025-08-18',
    #     adults='1',
    #     children='0',
    #     infants='0',
    #     travelClass='BUSINESS',
    #     max=2
    # )

    response = amadeus.reference_data.locations.hotels.by_city.get(
        cityCode="BKK",
        ratings="5",
        radius="5",
        radiusUnit="KM" 
    )

    print(response.result)
    print(response.body)
    print(response.data)

except ResponseError as error:
    print(error)
