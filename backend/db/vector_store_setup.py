import os
from dotenv import load_dotenv
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
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

