# SHL Conversational Assessment Recommender

A FastAPI-based conversational AI agent that recommends SHL Individual Test Solutions through grounded semantic retrieval and multi-turn dialogue.

## Features

- Conversational assessment recommendation
- Clarification for vague hiring requests
- Semantic search using Sentence Transformers + FAISS
- Grounded recommendations using official SHL catalog data
- Stateless conversation handling
- FastAPI REST API
- Off-topic and prompt injection refusal handling

---

## Architecture

```text
User Query
   ↓
Intent Extraction
   ↓
Semantic Retrieval (FAISS)
   ↓
Grounded SHL Catalog Matching
   ↓
Conversational Recommendation Response
