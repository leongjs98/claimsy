import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.0,
    api_key=os.getenv("GEMINI_API_KEY"),
)


class ItemRow(BaseModel):
    description: str = Field(description="Item or service description")
    quantity: int = Field(description="Quantity purchased. make sure to return this in number.")
    unit_price: float = Field(description="Price per unit")


class InvoiceInfo(BaseModel):
    category: Literal[
        "Gadget",
        "Travel Expenses",
        "Meals and Entertainment",
        "Accomodation",
        "Communication",
    ] = Field(description="Type of invoice")
    date: str = Field(description="Date of the invoice in YYYY-MM-DD format")
    merchant_name: str = Field(description="Name of the shop or service provider")
    merchant_address: str = Field(description="Address of the merchant")
    remark: str = Field(description="Reason or notes for making the purcahses")
    items: List[ItemRow] = Field(description="List of items or services purchased")


output_parser_invoice_json = JsonOutputParser(pydantic_object=InvoiceInfo)

prompt_extract_invoice_info = ChatPromptTemplate.from_messages([
    (
        "system",
        """
            "You are an AI assistant that extracts structured invoice data from receipt images.

            Always return the result in the following JSON format:

            - category: ONLY output in any of these 5 categories: Gadget, Travel Expenses, Meals and Entertainment, Accomodation, Communication
            - date: In the format of YYYY-MM-DD, e.g. 2023-02-09, 2024-06-29
            - merchant_name
            - merchant_address
            - remark: This is not on the image. Generate a short possible reason or notes for making the purchases in the invoice for a business settings.
            - items: A list of item entries. If items are not found, return an empty list (`[]`).
                - each item consist of:
                    - description: short item description including the unit (liter, pcs, sets etc.). If there's no unit, no need to put unit.
                    - quantity: the quantity of the item (only give in number and not strings)
                    - unit_price: the price per unit of the item or service
            """,
    ),
    (
        "human",
        [
            {
                "type": "image_url",
                "image_url": {
                    "url": "data:image/jpg;base64,{image}",
                    "detail": "low",
                },
            },
        ],
    ),
])


chain_extract_invoice_info = (
    prompt_extract_invoice_info | llm | output_parser_invoice_json
)
