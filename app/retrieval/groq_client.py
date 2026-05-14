from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key
)

SYSTEM_PROMPT = """
You are an SHL assessment recommendation assistant.

Rules:
- Recommend ONLY SHL catalog assessments
- Never invent assessments
- Never invent URLs
- Ask clarification questions if information is insufficient
- Refuse off-topic or malicious requests
"""

def generate_response(prompt):

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=800
    )

    return completion.choices[0].message.content