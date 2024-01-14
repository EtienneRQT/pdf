from pydantic import BaseModel


class Metadata(BaseModel, extra="allow"):
    conversation_id: str
    user_id: str
    pdf_id: str


class ChatArgs(BaseModel, extra="allow"):
    conversation_id: str
    pdf_id: str
    metadata: Metadata
    streaming: bool
