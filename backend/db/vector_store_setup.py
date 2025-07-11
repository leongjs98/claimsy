import os
from dotenv import load_dotenv
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from .postgresql_setup import GEMINI_API_KEY

load_dotenv()
MONGODB_ATLAS_CLUSTER_URI = os.getenv("MONGODB_ATLAS_CLUSTER_URI")
VECTOR_DB_NAME = os.getenv("VECTOR_DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
ATLAS_VECTOR_SEARCH_INDEX_NAME = os.getenv("ATLAS_VECTOR_SEARCH_INDEX_NAME")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY,
)


def client_setup():
    client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
    return client


def mongodb_collection_setup(client):
    MONGODB_COLLECTION = client[VECTOR_DB_NAME][COLLECTION_NAME]
    return MONGODB_COLLECTION


def vector_store_setup(client):
    """Remember to close"""

    MONGODB_COLLECTION = mongodb_collection_setup(client)
    vector_store = MongoDBAtlasVectorSearch(
        collection=MONGODB_COLLECTION,
        embedding=embeddings,
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
        relevance_score_fn="cosine",
    )

    return vector_store
