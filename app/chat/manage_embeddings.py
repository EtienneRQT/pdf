from typing import Iterable, List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from unstructured.cleaners.core import clean_extra_whitespace
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store


def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    loader = UnstructuredPDFLoader(
        file_path=pdf_path, post_processors=[clean_extra_whitespace]
    )
    docs: List[Document] = loader.load_and_split(text_splitter=text_splitter)

    for doc in docs:
        doc.metadata.update(
            {
                "text": doc.page_content,
                "pdf_id": pdf_id,
            }
        )

    vector_store.add_documents(documents=docs)


def delete_embeddings_for_pdf(pdf_id: str):
    vector_store.delete(filter={"pdf_id": pdf_id})
