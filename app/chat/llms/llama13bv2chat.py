from langchain_community.llms.replicate import Replicate
from langchain_community.llms import Replicate as ReplicateForCondensedQuestion
from app.chat.models import ChatArgs
import os


os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")  # type: ignore


def build_llm(chat_args: ChatArgs):
    return ReplicateForCondensedQuestion(
        model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
        streaming=chat_args.streaming,
    )


def build_llm_for_condensed_question():
    return Replicate(
        model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
        streaming=False,
    )
