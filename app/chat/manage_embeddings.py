from typing import Iterable, List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_openai import OpenAIEmbeddings
from unstructured.cleaners.core import (
    clean_extra_whitespace,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from app.chat.vector_stores.pinecone import vector_store
from app.chat.unstructured.categorize_elements import categorize_elements
from app.chat.unstructured.partition_pdf import pdf_elements
from app.chat.unstructured.generate_text_summaries import generate_text_summaries
from app.chat.unstructured.generate_image_summaries import generate_img_summaries
import app.chat.multi_vector_retriever.create_multi_vector_retriever as mvr
from app.chat.unstructured.multi_modal_rag_chain import multi_modal_rag_chain


def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    texts, tables = categorize_elements(pdf_elements)

    # Get text, table summaries
    text_summaries, table_summaries = generate_text_summaries(
        texts[9:], tables, summarize_texts=True
    )

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    # loader = UnstructuredPDFLoader(
    #     file_path=pdf_path,
    #     post_processors=[
    #         clean_extra_whitespace,
    #     ],
    # )

    # docs: List[Document] = loader.load_and_split(text_splitter=text_splitter)

    # for doc in docs:
    #     doc.metadata.update(
    #         {
    #             "text": doc.page_content,
    #             "pdf_id": pdf_id,
    #         }
    #     )

    # vector_store.add_documents(documents=docs)

    texts, tables = categorize_elements(pdf_elements)
    text_summaries2, table_summaries = generate_text_summaries(
        texts[9:], tables, summarize_texts=True
    )

    fpath = "./images"
    # Image summaries
    img_base64_list, image_summaries = generate_img_summaries(fpath)

    # The vectorstore to use to index the summaries
    vectorstore = Chroma(
        collection_name="mm_rag_mistral",
        embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
    )


def delete_embeddings_for_pdf(pdf_id: str):
    """Deletes embeddings for the given PDF ID.
    Args:
        pdf_id (str): The ID of the PDF to delete embeddings for.
    """
    vector_store.delete(filter={"pdf_id": pdf_id})
