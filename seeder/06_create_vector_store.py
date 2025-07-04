import os
import sys
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.vector_store_setup import MONGODB_ATLAS_CLUSTER_URI, VECTOR_DB_NAME, ATLAS_VECTOR_SEARCH_INDEX_NAME, COLLECTION_NAME, embeddings

load_dotenv()

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

MONGODB_COLLECTION = client[VECTOR_DB_NAME][COLLECTION_NAME]
vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

vector_store.create_vector_search_index(dimensions=768)

print(f"Vector Store: {VECTOR_DB_NAME} Created!")
client.close()
