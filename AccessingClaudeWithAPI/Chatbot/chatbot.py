"""Simple CLI chatbot using the Claude API with conversation history."""

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()  # Uses ANTHROPIC_API_KEY from environment
messages = []

print("Chat with Claude (type 'quit' to exit)\n")

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
    )

    assistant_reply = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_reply})

    print(f"\nClaude: {assistant_reply}\n")
