from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    role: str  # "customer" or "agent"
    text: str


class SentimentRequest(BaseModel):
    messages: List[Message]


class MessageResult(BaseModel):
    text: str
    label: str
    confidence: float


class SentimentResponse(BaseModel):
    overall_sentiment: str
    confidence: float
    analyzed_text: str
    used_messages: List[str]