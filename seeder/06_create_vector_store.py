import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.vector_store_setup import (
    VECTOR_DB_NAME,
    client_setup,
    vector_store_setup,
)

load_dotenv()

client = client_setup()
vector_store = vector_store_setup(client)

vector_store.create_vector_search_index(dimensions=768)

print(f"Vector Store: {VECTOR_DB_NAME} Created!")
client.close()
