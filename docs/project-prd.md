# Customer Sentiment Tracking System (PRD)

## Overview
We want to track customer satisfaction from chat conversations between agents and customers.

Currently, we don’t have a way to measure how satisfied customers are after interacting with support agents. This leads to poor service going unnoticed and customers leaving.

This system will analyze chat conversations and assign a sentiment score (positive, neutral, or negative) to help us understand customer experience.

---

## Goal
- Measure customer satisfaction automatically
- Identify poor agent performance
- Improve customer retention

---

## Problem
- Agents respond to chats, but quality is not tracked
- No visibility into customer frustration or satisfaction
- Difficult to know which agents are performing well

---

## Solution
- Receive chat data from Jivochat via webhook
- Analyze chat messages using an AI model
- Assign sentiment (positive, neutral, negative)
- Store results in a database
- Display insights on a dashboard

---

## Key Features

### 1. Sentiment Analysis
- Input: chat conversation
- Output:
  - Sentiment label (positive / neutral / negative)
  - Confidence score

---

### 2. Agent Performance Tracking
- Track sentiment per agent
- Identify agents with high negative interactions

---

### 3. Dashboard (Grafana)
- Daily sentiment trends
- Agent performance
- Percentage of negative chats

---

## Success Criteria
- Model correctly identifies obvious negative and positive chats
- Handles neutral cases like "it's okay" reasonably well
- Provides consistent signals (not perfect accuracy)

---

## Future Improvements
- Fine-tune model on company chat data
- Real-time sentiment tracking
- AI chatbot assistant for agents