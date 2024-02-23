import os
from langchain_community.vectorstores.qdrant import Qdrant
from qdrant_client import QdrantClient
from app.chat.embeddings.openai import embeddings
from app.chat.models import ChatArgs

url = os.getenv("QDRANT_URL")
api_key = os.getenv("'QDRANT_API_KEY")
collection_name = os.getenv("QDRANT_COLLECTION_NAME")
client = QdrantClient(url=url, api_key=api_key)
if collection_name:
    vector_store = Qdrant(
        client=client, collection_name=collection_name, embeddings=embeddings
    )


def build_retriever(chat_args: ChatArgs):
    """Retrieve a retriever instance for searching the vector store.
    Args:
      chat_args: Chat arguments containing context like pdf_id.
    Returns:
      A retriever instance if the vector_store is configured, else None.
    """
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}}
    if vector_store:
        return vector_store.as_retriever()
