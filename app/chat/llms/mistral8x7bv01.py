import os
from langchain_community.llms.deepinfra import DeepInfra

from app.chat.models import ChatArgs

os.environ["DEEPINFRA_API_TOKEN"] = os.getenv("DEEPINFRA_API_TOKEN")  # type: ignore


def build_llm(chat_args: ChatArgs):
    llm = DeepInfra(
        model_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    )

    llm.model_kwargs = {
        "temperature": 0.2,
        "repetition_penalty": 1.2,
        "max_new_tokens": 250,
        "top_p": 0.9,
        "stream": chat_args.streaming,
    }

    return llm


def build_llm_for_condensed_question():
    llm = DeepInfra(
        model_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    )

    llm.model_kwargs = {
        "temperature": 0.2,
        "repetition_penalty": 1.2,
        "max_new_tokens": 250,
        "top_p": 0.9,
    }

    return llm
