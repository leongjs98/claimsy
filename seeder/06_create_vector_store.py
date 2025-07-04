import os
import sys
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.postgresql_setup import GEMINI_API_KEY, MONGODB_ATLAS_CLUSTER_URI

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY,
)

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

DB_NAME = "claimsy_claim_policy_db"
COLLECTION_NAME = "claim_policy"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "claim-policy-index-1"
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

vector_store.create_vector_search_index(dimensions=768)

print("Claim Policy Vector Store Created!")
client.close()
