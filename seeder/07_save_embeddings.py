import os
import sys
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.vector_store_setup import (
    mongodb_collection_setup,
    client_setup,
    vector_store_setup,
)

CLAIM_POLICY_PDF = "./docs/claim_policy.pdf"

client = client_setup()
vector_store = vector_store_setup(client)
MONGODB_COLLECTION = mongodb_collection_setup(client)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

loader = PyPDFLoader(CLAIM_POLICY_PDF)
docs = loader.load_and_split(text_splitter=text_splitter)

MONGODB_COLLECTION.delete_many({})  # Delete existing data
vector_store.add_documents(docs)
print("Claim Policy PDF Added")
print("Check your MongoDB Cluster")
client.close()
