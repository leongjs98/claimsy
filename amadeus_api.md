## Get Access Token (Bearer)
```sh
curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}" | jq
```

## Search Flight
[Reference](https://admin.developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference)

```sh
curl 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SIN&destinationLocationCode=BKK&departureDate=2025-08-15&returnDate=2025-08-18&adults=1&children=0&infants=0&travelClass=BUSINESS&currencyCode=SGD&max=2' \
      -H 'Authorization: Bearer ABCDE123456789' | jq
```

Sample Output
```json
{
  "meta": {
    "count": 2,
    "links": {
      "self": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SIN&destinationLocationCode=BKK&departureDate=2025-08-15&returnDate=2025-08-18&adults=1&children=0&infants=0&travelClass=BUSINESS&currencyCode=SGD&max=2"
    }
  },
  "data": [
    {
      "type": "flight-offer",
      "id": "1",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-08-15",
      "lastTicketingDateTime": "2025-08-15",
      "numberOfBookableSeats": 5,
      "itineraries": [
        {
          "duration": "PT7H55M",
          "segments": [
            {
              "departure": {
                "iataCode": "SIN",
                "terminal": "3",
                "at": "2025-08-15T13:10:00"
              },
              "arrival": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-15T14:25:00"
              },
              "carrierCode": "VN",
              "number": "650",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT2H15M",
              "id": "1",
              "numberOfStops": 0,
              "blacklistedInEU": false
            },
            {
              "departure": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-15T18:30:00"
              },
              "arrival": {
                "iataCode": "BKK",
                "at": "2025-08-15T20:05:00"
              },
              "carrierCode": "VN",
              "number": "609",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT1H35M",
              "id": "2",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT5H5M",
          "segments": [
            {
              "departure": {
                "iataCode": "BKK",
                "at": "2025-08-18T11:20:00"
              },
              "arrival": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-18T13:05:00"
              },
              "carrierCode": "VN",
              "number": "600",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT1H45M",
              "id": "3",
              "numberOfStops": 0,
              "blacklistedInEU": false
            },
            {
              "departure": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-18T14:25:00"
              },
              "arrival": {
                "iataCode": "SIN",
                "terminal": "3",
                "at": "2025-08-18T17:25:00"
              },
              "carrierCode": "VN",
              "number": "655",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT2H",
              "id": "4",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "SGD",
        "total": "887.10",
        "base": "620.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "887.10"
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": [
        "VN"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "SGD",
            "total": "887.10",
            "base": "620.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "1",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            },
            {
              "segmentId": "2",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            },
            {
              "segmentId": "3",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            },
            {
              "segmentId": "4",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            }
          ]
        }
      ]
    },
    {
      "type": "flight-offer",
      "id": "2",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "isUpsellOffer": false,
      "lastTicketingDate": "2025-08-15",
      "lastTicketingDateTime": "2025-08-15",
      "numberOfBookableSeats": 5,
      "itineraries": [
        {
          "duration": "PT7H55M",
          "segments": [
            {
              "departure": {
                "iataCode": "SIN",
                "terminal": "3",
                "at": "2025-08-15T13:10:00"
              },
              "arrival": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-15T14:25:00"
              },
              "carrierCode": "VN",
              "number": "650",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT2H15M",
              "id": "1",
              "numberOfStops": 0,
              "blacklistedInEU": false
            },
            {
              "departure": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-15T18:30:00"
              },
              "arrival": {
                "iataCode": "BKK",
                "at": "2025-08-15T20:05:00"
              },
              "carrierCode": "VN",
              "number": "609",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT1H35M",
              "id": "2",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        },
        {
          "duration": "PT15H40M",
          "segments": [
            {
              "departure": {
                "iataCode": "BKK",
                "at": "2025-08-18T19:30:00"
              },
              "arrival": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-18T21:15:00"
              },
              "carrierCode": "VN",
              "number": "606",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT1H45M",
              "id": "5",
              "numberOfStops": 0,
              "blacklistedInEU": false
            },
            {
              "departure": {
                "iataCode": "SGN",
                "terminal": "2",
                "at": "2025-08-19T09:10:00"
              },
              "arrival": {
                "iataCode": "SIN",
                "terminal": "3",
                "at": "2025-08-19T12:10:00"
              },
              "carrierCode": "VN",
              "number": "651",
              "aircraft": {
                "code": "321"
              },
              "operating": {
                "carrierCode": "VN"
              },
              "duration": "PT2H",
              "id": "6",
              "numberOfStops": 0,
              "blacklistedInEU": false
            }
          ]
        }
      ],
      "price": {
        "currency": "SGD",
        "total": "887.10",
        "base": "620.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "887.10"
      },
      "pricingOptions": {
        "fareType": [
          "PUBLISHED"
        ],
        "includedCheckedBagsOnly": true
      },
      "validatingAirlineCodes": [
        "VN"
      ],
      "travelerPricings": [
        {
          "travelerId": "1",
          "fareOption": "STANDARD",
          "travelerType": "ADULT",
          "price": {
            "currency": "SGD",
            "total": "887.10",
            "base": "620.00"
          },
          "fareDetailsBySegment": [
            {
              "segmentId": "1",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            },
            {
              "segmentId": "2",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            },
            {
              "segmentId": "5",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            },
            {
              "segmentId": "6",
              "cabin": "BUSINESS",
              "fareBasis": "I1YAS",
              "class": "I",
              "includedCheckedBags": {
                "quantity": 1
              },
              "includedCabinBags": {
                "quantity": 2
              }
            }
          ]
        }
      ]
    }
  ],
  "dictionaries": {
    "locations": {
      "BKK": {
        "cityCode": "BKK",
        "countryCode": "TH"
      },
      "SIN": {
        "cityCode": "SIN",
        "countryCode": "SG"
      },
      "SGN": {
        "cityCode": "SGN",
        "countryCode": "VN"
      }
    },
    "aircraft": {
      "321": "AIRBUS A321"
    },
    "currencies": {
      "SGD": "SINGAPORE DOLLA"
    },
    "carriers": {
      "VN": "VIETNAM AIRLINES"
    }
  }
}
```

## Search Hotel
[Reference](https://developers.amadeus.com/self-service/category/hotels/api-doc/hotel-list/api-reference)

```sh
curl 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=BKK&ratings=5&radius=5&radiusUnit=KM' \
      -H 'Authorization: Bearer ABCDE123456789' | jq
```

sample output
```json
{
  "data": [
    {
      "chainCode": "IC",
      "iataCode": "BKK",
      "dupeId": 700012671,
      "name": "INTERCONTINENTAL BANGKOK",
      "hotelId": "ICBKKICB",
      "geoCode": {
        "latitude": 13.74572,
        "longitude": 100.54084
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10330",
        "cityName": "BANGKOK",
        "lines": [
          "973 PLOENCHIT ROAD"
        ]
      },
      "distance": {
        "value": 0.14,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "6C",
      "lastUpdate": "2025-06-03T10:19:57"
    },
    {
      "chainCode": "LX",
      "iataCode": "BKK",
      "dupeId": 700148499,
      "name": "HANSAR BANGKOK HOTEL",
      "hotelId": "LXBKKHBA",
      "geoCode": {
        "latitude": 13.74041,
        "longitude": 100.54077
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10330",
        "cityName": "BANGKOK",
        "lines": [
          "3 RAJDAMRI ROAD",
          "LUMPINI PATHUMWAN"
        ]
      },
      "distance": {
        "value": 0.46,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:16:32"
    },
    {
      "chainCode": "XR",
      "iataCode": "BKK",
      "dupeId": 700141971,
      "name": "THE ST REGIS BANGKOK",
      "hotelId": "XRBKK199",
      "geoCode": {
        "latitude": 13.73977,
        "longitude": 100.54002
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10330",
        "cityName": "BANGKOK",
        "lines": [
          "159 RAJADAMRI ROAD"
        ]
      },
      "distance": {
        "value": 0.53,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "EM",
      "lastUpdate": "2025-06-03T10:18:38"
    },
    {
      "chainCode": "HS",
      "iataCode": "BKK",
      "dupeId": 700056249,
      "name": "AMARI RESIDENCES BANGKOK",
      "hotelId": "HSBKKAHS",
      "geoCode": {
        "latitude": 13.74104,
        "longitude": 100.54359
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10330",
        "cityName": "BANGKOK",
        "lines": [
          "43 SOI LANGSUAN, PLOENCHIT ROAD, LUMPINI"
        ]
      },
      "distance": {
        "value": 0.53,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:17:48"
    },
    {
      "chainCode": "RT",
      "iataCode": "BKK",
      "dupeId": 700152794,
      "name": "HOTEL MUSE BANGKOK",
      "hotelId": "RTBKKMGA",
      "geoCode": {
        "latitude": 13.74006,
        "longitude": 100.54339
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10330",
        "cityName": "BANGKOK",
        "lines": [
          "55 555 LANGSUAN ROAD",
          "PLOENCHIT ROAD"
        ]
      },
      "distance": {
        "value": 0.6,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:17:18"
    },
    {
      "chainCode": "LW",
      "iataCode": "BKK",
      "dupeId": 700171249,
      "name": "THE OKURA PRESTIGE BANGKOK",
      "hotelId": "LWBKK832",
      "geoCode": {
        "latitude": 13.74273,
        "longitude": 100.54777
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10330",
        "cityName": "BANGKOK",
        "lines": [
          "PARK VENTURES ECOPLEX",
          "57 WIRELESS ROAD"
        ]
      },
      "distance": {
        "value": 0.84,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:20:27"
    },
    {
      "chainCode": "RT",
      "iataCode": "BKK",
      "dupeId": 700082359,
      "name": "VIE HOTEL BANGKOK MGALLERY",
      "hotelId": "RTBKKVIE",
      "geoCode": {
        "latitude": 13.75057,
        "longitude": 100.53204
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10400",
        "cityName": "BANGKOK",
        "lines": [
          "117-39 PHAYA THAI ROAD",
          "RATCHATHEWI"
        ]
      },
      "distance": {
        "value": 1.11,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:17:18"
    },
    {
      "chainCode": "MC",
      "iataCode": "BKK",
      "dupeId": 700008853,
      "name": "JW MARRIOTT HOTEL BANGKOK",
      "hotelId": "MCBKKDTM",
      "geoCode": {
        "latitude": 13.74266,
        "longitude": 100.55186
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "4 SUKHUMVIT SOI 2"
        ]
      },
      "distance": {
        "value": 1.27,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "EM",
      "lastUpdate": "2025-06-03T10:17:42"
    },
    {
      "chainCode": "BW",
      "iataCode": "BKK",
      "dupeId": 700162121,
      "name": "BEST WESTERN PREMIER SUKHUMVIT",
      "hotelId": "BWBKK356",
      "geoCode": {
        "latitude": 13.74677,
        "longitude": 100.55181
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "78 SUKHUMVIT SOI 1",
          "KLONGTOEY NUA WATTANA"
        ]
      },
      "distance": {
        "value": 1.27,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "EW",
      "lastUpdate": "2025-06-03T10:16:09"
    },
    {
      "chainCode": "XT",
      "iataCode": "BKK",
      "dupeId": 700042345,
      "name": "MAJESTIC GRANDE HOTEL",
      "hotelId": "XTBKK372",
      "geoCode": {
        "latitude": 13.74074,
        "longitude": 100.55166
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "12 SUKHUMVIT 2"
        ]
      },
      "distance": {
        "value": 1.3,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:18:40"
    },
    {
      "chainCode": "YX",
      "iataCode": "BKK",
      "dupeId": 700162420,
      "name": "GRANDE CENTRE POINT T 21",
      "hotelId": "YXBKKGCP",
      "geoCode": {
        "latitude": 13.74216,
        "longitude": 100.55304
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "2 88 SUKHUMVIT SOI 19",
          "SUKHUMVIT ROAD -KLONGTOEY NUA"
        ]
      },
      "distance": {
        "value": 1.41,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:18:44"
    },
    {
      "chainCode": "WV",
      "iataCode": "BKK",
      "dupeId": 700012670,
      "name": "THE SUKOSOL BANGKOK",
      "hotelId": "WVBKKSCH",
      "geoCode": {
        "latitude": 13.75789,
        "longitude": 100.53604
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10400",
        "cityName": "PHAYA THAI",
        "lines": [
          "477 SI AYUTHAYA ROAD"
        ]
      },
      "distance": {
        "value": 1.55,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "TC",
      "lastUpdate": "2025-06-03T10:18:08"
    },
    {
      "chainCode": "FG",
      "iataCode": "BKK",
      "dupeId": 700013406,
      "name": "MONTIEN HOTEL BANGKOK",
      "hotelId": "FGBKKMHB",
      "geoCode": {
        "latitude": 13.73046,
        "longitude": 100.5311
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10500",
        "cityName": "BANGKOK",
        "lines": [
          "54 SURAWONGSE ROAD"
        ]
      },
      "distance": {
        "value": 1.85,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:16:31"
    },
    {
      "chainCode": "SB",
      "iataCode": "BKK",
      "dupeId": 700079671,
      "name": "SOFITEL BANGKOK SUKHUMVIT",
      "hotelId": "SBBKKSKV",
      "geoCode": {
        "latitude": 13.73977,
        "longitude": 100.55769
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "SUKHUMVIT ROAD SOI 13-15",
          "KLONGTOEY WATTANA"
        ]
      },
      "distance": {
        "value": 1.96,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:17:28"
    },
    {
      "chainCode": "KI",
      "iataCode": "BKK",
      "dupeId": 700141339,
      "name": "SIAM KEMPINSKI BANGKOK",
      "hotelId": "KIBKKSIA",
      "geoCode": {
        "latitude": 13.74867,
        "longitude": 100.5223
      },
      "address": {
        "countryCode": "TH",
        "cityName": "BANGKOK",
        "lines": [
          "991/9 RAMA 1 ROAD"
        ]
      },
      "distance": {
        "value": 1.99,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "GL",
      "lastUpdate": "2025-06-03T10:20:29"
    },
    {
      "chainCode": "IQ",
      "iataCode": "BKK",
      "dupeId": 700163782,
      "name": "THE AETAS LUMPINI",
      "hotelId": "IQBKKATL",
      "geoCode": {
        "latitude": 13.72535,
        "longitude": 100.54236
      },
      "address": {
        "countryCode": "TH",
        "cityName": "BANGKOK",
        "lines": [
          "1030/4 RAMA 4 ROAD",
          "THUNGMAHAMEK, SATHORN"
        ]
      },
      "distance": {
        "value": 2.14,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:16:45"
    },
    {
      "chainCode": "MU",
      "iataCode": "BKK",
      "dupeId": 700054159,
      "name": "GRAND MILLENNIUM SUKHUMVIT BANGKOK",
      "hotelId": "MUBKKMSB",
      "geoCode": {
        "latitude": 13.73842,
        "longitude": 100.55932
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "30 SUKHUMVIT 21 ASOKE ROAD"
        ]
      },
      "distance": {
        "value": 2.17,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:20:23"
    },
    {
      "chainCode": "RT",
      "iataCode": "BKK",
      "dupeId": 700132030,
      "name": "GRAND MERCURE ASOKE RESIDENCE",
      "hotelId": "RTBKKASO",
      "geoCode": {
        "latitude": 13.74167,
        "longitude": 100.56083
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "50 5 SUKHUMVIT SOI 19",
          "WATTANA DISTRICT"
        ]
      },
      "distance": {
        "value": 2.25,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:17:18"
    },
    {
      "chainCode": "BY",
      "iataCode": "BKK",
      "dupeId": 700021182,
      "name": "BANYAN TREE BANGKOK",
      "hotelId": "BYBKK800",
      "geoCode": {
        "latitude": 13.72349,
        "longitude": 100.53988
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10120",
        "cityName": "BANGKOK",
        "lines": [
          "21 100 SOUTH SATHON ROAD"
        ]
      },
      "distance": {
        "value": 2.34,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:19:21"
    },
    {
      "chainCode": "HS",
      "iataCode": "BKK",
      "dupeId": 700071977,
      "name": "URBANA SATHORN",
      "hotelId": "HSBKKAMO",
      "geoCode": {
        "latitude": 13.72289,
        "longitude": 100.53608
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10120",
        "cityName": "BANGKOK",
        "lines": [
          "55 SOUTH SATHORN ROAD, TUNGMAHAMEK"
        ]
      },
      "distance": {
        "value": 2.45,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:17:47"
    },
    {
      "chainCode": "UZ",
      "iataCode": "BKK",
      "dupeId": 700165162,
      "name": "THE CONTINENT HOTEL",
      "hotelId": "UZBKK969",
      "geoCode": {
        "latitude": 13.73622,
        "longitude": 100.562
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "413 SUKHUMVIT ROAD, NEAR ASOKE BTS STATION AND",
          "SUKHUMVIT MRT STATION"
        ]
      },
      "distance": {
        "value": 2.53,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:18:05"
    },
    {
      "chainCode": "PU",
      "iataCode": "BKK",
      "dupeId": 700002574,
      "name": "PULLMAN BANGKOK HOTEL G",
      "hotelId": "PUBKKMON",
      "geoCode": {
        "latitude": 13.7258,
        "longitude": 100.52593
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10500",
        "cityName": "BANGKOK",
        "lines": [
          "188 SILOM ROAD",
          "BANGRAK"
        ]
      },
      "distance": {
        "value": 2.59,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:16:57"
    },
    {
      "chainCode": "RT",
      "iataCode": "BKK",
      "dupeId": 700085146,
      "name": "IBIS BANGKOK SATHORN",
      "hotelId": "RTBKKSAT",
      "geoCode": {
        "latitude": 13.72164,
        "longitude": 100.54672
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10120",
        "cityName": "BANGKOK",
        "lines": [
          "SOI NGAM DUPHLI RAMA IV",
          "SATHORN"
        ]
      },
      "distance": {
        "value": 2.64,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "RT",
      "lastUpdate": "2025-06-03T10:17:18"
    },
    {
      "chainCode": "WH",
      "iataCode": "BKK",
      "dupeId": 700183608,
      "name": "W BANGKOK",
      "hotelId": "WHBKK258",
      "geoCode": {
        "latitude": 13.72221,
        "longitude": 100.52902
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10500",
        "cityName": "BANGKOK",
        "lines": [
          "106 NORTH SATHORN ROAD",
          "SILOM BANGRAK"
        ]
      },
      "distance": {
        "value": 2.76,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "EM",
      "lastUpdate": "2025-06-03T10:18:01"
    },
    {
      "chainCode": "WK",
      "iataCode": "BKK",
      "dupeId": 700002568,
      "name": "REMBRANDT HOTEL BANGKOK",
      "hotelId": "WKBKKREM",
      "geoCode": {
        "latitude": 13.73294,
        "longitude": 100.5631
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "19 SUKHUMVIT SOI 18",
          "SUKHUMVIT ROAD KLONG TOEY"
        ]
      },
      "distance": {
        "value": 2.79,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "TC",
      "lastUpdate": "2025-06-03T10:18:07"
    },
    {
      "chainCode": "RD",
      "iataCode": "BKK",
      "dupeId": 700217197,
      "name": "RADISSON BLU PLAZA BANGKOK",
      "hotelId": "RDBKK591",
      "geoCode": {
        "latitude": 13.73463,
        "longitude": 100.5641
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "489 SUKHUMVIT ROAD KLONGTOEY N"
        ]
      },
      "distance": {
        "value": 2.8,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "CW",
      "lastUpdate": "2025-06-03T10:17:12"
    },
    {
      "chainCode": "LX",
      "iataCode": "BKK",
      "dupeId": 700140849,
      "name": "S31 SUKHUMVIT HOTEL",
      "hotelId": "LXBKKSKT",
      "geoCode": {
        "latitude": 13.73369,
        "longitude": 100.56628
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "545 SUKHUMVIT 31"
        ]
      },
      "distance": {
        "value": 3.06,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:16:03"
    },
    {
      "chainCode": "PF",
      "iataCode": "BKK",
      "dupeId": 700028919,
      "name": "PAN PACIFIC SERVICED SUITES BANGKOK",
      "hotelId": "PFBKKPSB",
      "geoCode": {
        "latitude": 13.7308,
        "longitude": 100.56948
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "88/333 SUKHUMVIT SOI 55",
          "NORTH KONGTON"
        ]
      },
      "distance": {
        "value": 3.51,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "GL",
      "lastUpdate": "2025-06-03T10:16:39"
    },
    {
      "chainCode": "UZ",
      "iataCode": "BKK",
      "dupeId": 700028920,
      "name": "THE DAVIS BANGKOK",
      "hotelId": "UZBKKDBK",
      "geoCode": {
        "latitude": 13.72105,
        "longitude": 100.56601
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10110",
        "cityName": "BANGKOK",
        "lines": [
          "88 SUKHUMVIT 24 KLONGTEOY"
        ]
      },
      "distance": {
        "value": 3.82,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:18:05"
    },
    {
      "chainCode": "WV",
      "iataCode": "BKK",
      "dupeId": 700154503,
      "name": "EASTIN GRAND HOTEL SATHORN",
      "hotelId": "WVBKK941",
      "geoCode": {
        "latitude": 13.71777,
        "longitude": 100.51712
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10120",
        "cityName": "BANGKOK",
        "lines": [
          "33/1 SOUTH SATHORN ROAD YANNAWA SATHORN"
        ]
      },
      "distance": {
        "value": 3.88,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "TC",
      "lastUpdate": "2025-06-03T10:18:08"
    },
    {
      "chainCode": "PN",
      "iataCode": "BKK",
      "dupeId": 700013450,
      "name": "THE PENINSULA BANGKOK",
      "hotelId": "PNBKK831",
      "geoCode": {
        "latitude": 13.72484,
        "longitude": 100.49556
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10600",
        "cityName": "BANGKOK",
        "lines": [
          "333 CHAROENNAKORN RD KLONGSAN"
        ]
      },
      "distance": {
        "value": 5.3,
        "unit": "KM"
      },
      "rating": 5,
      "lastUpdate": "2025-06-03T10:16:53"
    },
    {
      "chainCode": "PH",
      "iataCode": "BKK",
      "dupeId": 700162994,
      "name": "THE SIAM BANGKOK PREFERRED",
      "hotelId": "PHBKKTSI",
      "geoCode": {
        "latitude": 13.78101,
        "longitude": 100.50612
      },
      "address": {
        "countryCode": "TH",
        "postalCode": "10300",
        "cityName": "BANGKOK",
        "lines": [
          "3/2 THANON KHAO",
          "VACHIRAPAYABAL"
        ]
      },
      "distance": {
        "value": 5.48,
        "unit": "KM"
      },
      "rating": 5,
      "masterChainCode": "PV",
      "lastUpdate": "2025-06-03T10:16:42"
    }
  ],
  "meta": {
    "count": 32,
    "links": {
      "self": "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=BKK&radius=5&radiusUnit=KM&ratings=5"
    }
  }
}
```

# Not used

## Search Transport/Transfer
[Reference](https://developers.amadeus.com/self-service/category/cars-and-transfers/api-doc/transfer-search/api-reference)

```sh
curl 'https://test.api.amadeus.com/v1/shopping/transfer-offers' \
      -H 'Content-Type: application/json' \
      --data '{
        "startLocationCode": "CDG",
        "endAddressLine": "Avenue Anatole France, 5",
        "endCityName": "Paris",
        "endZipCode": "75007",
        "endCountryCode": "FR",
        "endName": "Souvenirs De La Tour",
        "endGeoCode": "48.859466,2.2976965",
        "transferType": "PRIVATE",
        "startDateTime": "2024-04-10T10:30:00",
        "passengers": 2,
        "stopOvers": [
          {
            "duration": "PT2H30M",
            "sequenceNumber": 1,
            "addressLine": "Avenue de la Bourdonnais, 19",
            "countryCode": "FR",
            "cityName": "Paris",
            "zipCode": "75007",
            "name": "De La Tours",
            "geoCode": "48.859477,2.2976985",
            "stateCode": "FR"
          }
        ],
        "startConnectedSegment": {
          "transportationType": "FLIGHT",
          "transportationNumber": "AF380",
          "departure": {
            "localDateTime": "2024-04-10T09:00:00",
            "iataCode": "NCE"
          },
          "arrival": {
            "localDateTime": "2024-04-10T10:00:00",
            "iataCode": "CDG"
          }
        },
        "passengerCharacteristics": [
          {
            "passengerTypeCode": "ADT",
            "age": 20
          },
          {
            "passengerTypeCode": "CHD",
            "age": 10
          }
        ]
      }' \
      -H 'Authorization: Bearer ABCDE123456789' | jq
```

## Flight Pricing
[Reference](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-price/api-reference)

```sh
curl 'https://test.api.amadeus.com/v1/shopping/flight-offers/pricing' \
      -H 'Content-Type: application/json' \
      --data '' \
      -H 'Authorization: Bearer ABCDE123456789' | jq
```

