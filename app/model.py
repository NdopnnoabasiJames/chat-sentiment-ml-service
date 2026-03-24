from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

print("Loading sentiment model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

model.eval()

labels = ["negative", "neutral", "positive"]

print("Model loaded successfully.")


def predict_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)

    confidence, predicted_class = torch.max(probs, dim=1)

    return {
        "label": labels[predicted_class.item()],
        "confidence": round(confidence.item(), 4)
    }


def predict_conversation(messages: list):
    # Step 1: keep only customer messages
    customer_msgs = [m.get("text", "").lower() for m in messages if m.get("role") == "customer"]

    # Step 2: filter out weak/meaningless messages
    ignore = ["ok", "okay", "thanks", "thank you", "alright", "hmm", "k"]

    meaningful_msgs = []
    for msg in customer_msgs:
        clean = msg.strip()
        if clean and clean not in ignore:
            meaningful_msgs.append(clean)

    # fallback if everything was filtered out
    if not meaningful_msgs:
        meaningful_msgs = customer_msgs[-1:] if customer_msgs else [""]

    # Step 3: take last 3 meaningful messages
    last_msgs = meaningful_msgs[-3:]

    # Step 4: combine into one text
    combined_text = ". ".join(last_msgs)

    # Step 5: predict once
    result = predict_sentiment(combined_text)

    return {
        "overall_sentiment": result["label"],
        "confidence": result["confidence"],
        "analyzed_text": combined_text,
        "used_messages": last_msgs
    }


if __name__ == "__main__":
    sample = "This is not bad at all"
    result = predict_sentiment(sample)
    print(result)