# Technical PRD - Customer Sentiment System

## Architecture

Jivochat → NestJS → FastAPI → ML Model → Database → Grafana

---

## Components

### 1. Jivochat
- Sends chat data via webhook

---

### 2. NestJS Backend
Responsibilities:
- Receive webhook data
- Extract chat messages
- Call FastAPI service
- Store results in database

---

### 3. FastAPI (ML Service)
Responsibilities:
- Load pretrained sentiment model
- Run inference on text
- Return sentiment + confidence

Model:
- cardiffnlp/twitter-roberta-base-sentiment-latest

---

### 4. Database (PostgreSQL - Supabase)

Tables:

#### chats
- id
- agent_id
- message
- created_at

#### sentiment_results
- id
- chat_id
- sentiment (positive/neutral/negative)
- confidence
- created_at

---

### 5. Dashboard (Grafana)
- Connect to PostgreSQL
- Visualize:
  - sentiment trends
  - agent performance

---

## API Design

### FastAPI

POST /predict

Request:
{
  "text": "customer message"
}

Response:
{
  "label": "negative",
  "confidence": 0.87
}

---

## Folder Structure

project-root/
│
├── fastapi-service/
│   ├── app/
│   │   ├── main.py
│   │   ├── model.py
│   │   └── schemas.py
│   ├── requirements.txt
│
├── nestjs-backend/
│
├── docs/
│   ├── product-prd.md
│   └── technical-prd.md

---

## Deployment Plan

- FastAPI → Render
- NestJS → Render
- Database → Supabase
- Dashboard → Grafana Cloud

---

## Model Strategy

Phase 1:
- Use pretrained model

Phase 2:
- Fine-tune on company data