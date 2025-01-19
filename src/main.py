import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

def chat_with_claude(user_input: str) -> str:
    """Send a message to claude and get a response"""
    client = Anthropic()

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            {
                "role": "user", 
                "content": user_input
            }
        ]
    )

    return message.content[0].text

def main():
    print("🤖 Welcome to Claude Chat!")
    print("Type 'quit' to exit")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            response = chat_with_claude(user_input)
            print(f"\nClaude: {response}")

        except Exception as e:
            print(f"❌ Oops! Something went wrong: {str(e)}")

if __name__ == "__main__":
    main()