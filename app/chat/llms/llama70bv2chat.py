from langchain_community.llms import DeepInfra
from langchain_community.llms import DeepInfra as ReplicateForCondensedQuestion
from app.chat.models import ChatArgs
import os


os.environ["DEEPINFRA_API_TOKEN"] = os.getenv("DEEPINFRA_API_TOKEN")  # type: ignore


def build_llm(chat_args: ChatArgs):
    llm = DeepInfra(
        model_id="meta-llama/Llama-2-70b-chat-hf",
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
    llm = ReplicateForCondensedQuestion(
        model_id="meta-llama/Llama-2-70b-chat-hf",
    )

    llm.model_kwargs = {
        "temperature": 0.2,
        "repetition_penalty": 1.2,
        "max_new_tokens": 250,
        "top_p": 0.9,
        "stream": False,
    }

    return llm