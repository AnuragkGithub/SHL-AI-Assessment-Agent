from app.agent.intent_parser import extract_intent
from app.retrieval.hybrid_search import search_catalog


def process_chat(messages):

    intent = extract_intent(messages)

    latest_user_message = ""

    for m in reversed(messages):
        if m.role == "user":
            latest_user_message = m.content.lower()
            break

    # Off-topic protection
    blocked_topics = [
        "salary",
        "legal",
        "immigration",
        "visa",
        "politics"
    ]

    if any(x in latest_user_message for x in blocked_topics):
        return {
            "reply": "I can only help with SHL assessment recommendations and comparisons.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Clarification stage
    if not intent.get("role"):
        return {
            "reply": "What role are you hiring for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if not intent.get("seniority"):
        return {
            "reply": "What seniority level are you targeting?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Retrieve recommendations
    recommendations = search_catalog(intent, top_k=5)

    # Confirmation detection
    confirmation_words = [
        "perfect",
        "thanks",
        "thank you",
        "looks good",
        "that's what we need",
        "great"
    ]

    end_flag = any(
        word in latest_user_message
        for word in confirmation_words
    )

    return {
        "reply": f"I found {len(recommendations)} SHL assessments relevant to your hiring needs.",
        "recommendations": recommendations,
        "end_of_conversation": end_flag
    }