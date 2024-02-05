from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOpenAI


def image_summarize(img_base64, prompt):
    """Make image summary"""
    model = ChatOpenAI(model_name="gpt-4", temperature=0, max_output_tokens=1024)

    msg = model(
        [
            HumanMessage(
                content=[
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"},
                    },
                ]
            )
        ]
    )
    return msg.content
