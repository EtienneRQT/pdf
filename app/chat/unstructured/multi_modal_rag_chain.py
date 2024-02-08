from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from app.chat.llms.GPT4 import ChatOpenAI
from app.chat.unstructured.split_image_text_type import split_image_text_types
from app.chat.unstructured.image_prompt_fun import img_prompt_func
from langchain.schema.output_parser import StrOutputParser


def multi_modal_rag_chain(retriever):
    """
    Multi-modal RAG chain
    """

    # Multi-modal LLM
    model = ChatOpenAI(
        temperature=0, model_name="gemini-pro-vision", max_output_tokens=1024
    )

    # RAG pipeline
    chain = (
        {
            "context": retriever | RunnableLambda(split_image_text_types),
            "question": RunnablePassthrough(),
        }
        | RunnableLambda(img_prompt_func)
        | model
        | StrOutputParser()
    )

    return chain
