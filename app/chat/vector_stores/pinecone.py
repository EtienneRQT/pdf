import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings


api_key = os.getenv("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENV_NAME")
if api_key and environment:
    pinecone.init(api_key=api_key, environment=environment)

index_name = os.getenv("PINECONE_INDEX_NAME")
if index_name:
    vector_store = Pinecone.from_existing_index(index_name, embeddings)
