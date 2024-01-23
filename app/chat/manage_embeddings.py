from typing import Iterable, List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store


def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    # Use PyPDFLoader to load the PDF and split it into pages.
    # TODO: Use PyMuPDFLoader instead of PyPDFLoader.
    loader = PyMuPDFLoader(file_path=pdf_path)
    docs: List[Document] = loader.load_and_split(text_splitter=text_splitter)

    for doc in docs:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
            "pdf_id": pdf_id,
        }

    vector_store.add_documents(documents=docs)


def delete_embeddings_for_pdf(pdf_id: str):
    vector_store.delete(filter={"pdf_id": pdf_id})
