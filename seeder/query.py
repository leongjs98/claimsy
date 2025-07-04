import os
import sys
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db.postgresql_setup import GEMINI_API_KEY
from backend.db.vector_store_setup import (
    client_setup,
    vector_store_setup,
)

client = client_setup()
vector_store = vector_store_setup(client)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
)

retriever = vector_store.as_retriever()
system_prompt = """
        Use the given context to answer the question.
        If you don't know the answer, say you don't know.
        Use three sentence maximum and keep the answer concise.
        Context: {context}
        """

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

document_chain = create_stuff_documents_chain(llm, prompt)
chain = create_retrieval_chain(retriever, document_chain)
ai_response = chain.invoke({"input": "how much can I claim for business meals?"})
print(ai_response["answer"])

client.close()
