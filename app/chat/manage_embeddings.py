from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.azure_ai_search import vector_store


def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    loader = PyMuPDFLoader(
        file_path=pdf_path,
    )

    docs: List[Document] = loader.load_and_split(text_splitter=text_splitter)

    for doc in docs:
        doc.metadata = (
            {
                "page" : doc.metadata["page"],
                "text": doc.page_content,
                "pdf_id": pdf_id,
            }
        )

    vector_store.add_documents(documents=docs)


def delete_embeddings_for_pdf(pdf_id: str):
    vector_store.delete(filter={"pdf_id": pdf_id})
