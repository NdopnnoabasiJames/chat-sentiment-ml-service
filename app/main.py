from fastapi import FastAPI
from app.schemas import SentimentRequest, SentimentResponse
from app.model import predict_conversation

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Sentiment API is running"}


@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    # Filter only customer messages
    customer_messages = [msg.text for msg in request.messages if msg.role.lower() == "customer"]

    # Fallback: if no customer messages, use all messages
    if not customer_messages:
        customer_messages = [msg.text for msg in request.messages]

    messages_payload = [{"text": text} for text in customer_messages]

    result = predict_conversation(messages_payload)
    return result