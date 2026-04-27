"""Simple Math tutor chatbot using the Claude API with conversation history. This focuses on system prompts"""

import sys

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()  # Uses ANTHROPIC_API_KEY from environment
messages = []

print("Chat with Claude (type 'quit' to exit)\n")

user_system_prompt = input("System prompt: ").strip()
if user_system_prompt.lower() in {"quit", "exit"}:
    sys.exit()
if not user_system_prompt:
    user_system_prompt = None


while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"quit", "exit"}:
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "claude-opus-4-7",
        "max_tokens": 1024,
        "messages": messages,
    }

    if user_system_prompt:
        payload["system"] = user_system_prompt

    response = client.messages.create(**payload)

    assistant_reply = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_reply})

    print(f"\nClaude: {assistant_reply}\n")
