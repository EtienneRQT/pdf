from app.chat.vector_stores.pinecone import build_retriever
from langchain.chains import ConversationalRetrievalChain
from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory


def build_chat(chat_args):
    retriever = build_retriever(chat_args)
    llm = build_llm(chat_args)
    memory = build_memory(chat_args)

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=retriever,  # type: ignore
    )
