from langchain_community.vectorstores.chroma import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecone import build_retriever
from app.chat.llms.GPT4 import build_llm, build_llm_for_condensed_question
from app.chat.memories.sql_memory import build_memory
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from app.chat.unstructured.multi_modal_rag_chain import multi_modal_rag_chain
from app.chat.unstructured.generate_text_summaries import generate_text_summaries
from app.chat.unstructured.generate_image_summaries import generate_img_summaries
from app.chat.multi_vector_retriever.create_multi_vector_retriever import (
    create_multi_vector_retriever,
)
from app.chat.unstructured.categorize_elements import categorize_elements
from app.chat.unstructured.partition_pdf import pdf_elements


def build_chat(chat_args: ChatArgs):
    """
    Builds a conversational chatbot agent using a retrieval chain.

    First, initializes the necessary components:
    - Retriever for retrieving relevant documents
    - LLMs for generating responses
    - Memory for tracking conversation state
    - Vectorstore and multi-vector retriever for handling multi-modal input
    - Chains for chaining different capabilities like RAG for unstructured data

    Then generates summaries of text, tables, images to index for retrieval.
    Invokes the multi-modal RAG chain on a sample query to demonstrate usage.

    Finally, returns a StreamingConversationalRetrievalChain instance that combines all of these components.
    """
    retriever = build_retriever(chat_args)
    llm = build_llm(chat_args)
    condense_question_llm = build_llm_for_condensed_question()
    memory = build_memory(chat_args)

    # Image summaries
    fpath = "./images"
    img_base64_list, image_summaries = generate_img_summaries(fpath)

    texts, tables = categorize_elements(pdf_elements)
    text_summaries2, table_summaries = generate_text_summaries(
        texts[9:], tables, summarize_texts=True
    )

    # Get text, table summaries
    text_summaries, table_summaries = generate_text_summaries(
        texts[9:], tables, summarize_texts=True
    )

    # The vectorstore to use to index the summaries
    vectorstore = Chroma(
        collection_name="mm_rag_mistral",
        embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
    )

    retriever_multi_vector_img = create_multi_vector_retriever(
        vectorstore,
        text_summaries,
        texts,
        table_summaries,
        tables,
        image_summaries,
        img_base64_list,
    )

    chain_multimodal_rag = multi_modal_rag_chain(retriever_multi_vector_img)
    query = """compare and contrast between mistral and llama2 across benchmarks and 
    explain the reasoning in detail"""
    docs = retriever_multi_vector_img.get_relevant_documents(query, limit=1)
    docs[0]
    chain_multimodal_rag.invoke(query)

    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever,  # type: ignore
        metadata=chat_args.metadata,
    )
