from langchain_community.chat_models import ChatOpenAI


def build_llm(chat_args):
    return ChatOpenAI(streaming=chat_args.streaming, model_name="gpt-3.5-turbo")


def build_llm_for_condensed_question():
    return ChatOpenAI(model_name="gpt-3.5-turbo")
