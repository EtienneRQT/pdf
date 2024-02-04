from typing import Iterable, List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from unstructured.partition.pdf import partition_pdf
from unstructured.cleaners.core import (
    clean_extra_whitespace,
    clean_bullets,
    group_broken_paragraphs,
    auto_paragraph_grouper,
    clean_dashes,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store


def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    loader = UnstructuredPDFLoader(
        file_path=pdf_path,
        post_processors=[
            clean_extra_whitespace,
            clean_bullets,
            group_broken_paragraphs,
            auto_paragraph_grouper,
            clean_dashes,
        ],
    )
    elements = partition_pdf(
        filename="pdf_path",
        strategy="hi_res",
        extract_images_in_pdf=True,
        extract_image_block_types=["Image", "Table"],
        extract_image_block_to_payload=False,
        extract_image_block_output_dir="../images",
    )

    texts, tables = categorize_elements(elements)

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


def categorize_elements(raw_pdf_elements):
    """
    Categorize extracted elements from a PDF into tables and texts.
    raw_pdf_elements: List of unstructured.documents.elements
    """
    tables = []
    texts = []
    for element in raw_pdf_elements:
        if "unstructured.documents.elements.Table" in str(type(element)):
            tables.append(str(element))
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            texts.append(str(element))
    return texts, tables
