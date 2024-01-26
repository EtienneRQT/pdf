import os
from pinecone import Pinecone as PineconeClient, ServerlessSpec
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings
from app.chat.models import ChatArgs


api_key = os.getenv("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENV_NAME")
if api_key and environment:
    pinecone = PineconeClient(api_key=api_key, environment=environment)


index_name = os.getenv("PINECONE_INDEX_NAME")
if index_name:
    vector_store: Pinecone = Pinecone.from_existing_index(index_name, embeddings)


def build_retriever(chat_args: ChatArgs):
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}}
    if vector_store:
        return vector_store.as_retriever(search_kwargs=search_kwargs)
