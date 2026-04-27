"""Simple Math tutor chatbot using the Claude API with conversation history. This focuses on system prompts"""

import sys

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()  # Uses ANTHROPIC_API_KEY from environment
messages = []

system_prompt = """
    You are a patient math tutor.
    Do not directly answer a student's questions.
    Guide them to a solution step by step.
"""

print("Chat with Claude Math Tutor (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"quit", "exit"}:
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=messages,
        system=system_prompt,
    )

    assistant_reply = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_reply})

    print(f"\nClaude Math Tutor: {assistant_reply}\n")
