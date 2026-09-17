from .api_client import create_client, get_ai_response
from .prompts import build_messages
from .utils import (
    clean_input,
    is_empty_input,
    is_exit_command,
    get_reply,
    get_error_message
)

#get user's message and clean it
def get_user_input():
    user_input = input("You: ")

    return clean_input(user_input)

#display the response
def display_response(text):
    print(f"Bot: {text}")

#running chatbot
def run_chatbot():
    print("Smart AI Chatbot")
    print("-" * 30)
    print("Type 'exit' to end the conversation.\n")

    # Create the Hugging Face client
    try:
        client = create_client()

    except Exception as e:
        print(f"Error: {get_error_message(e)}")
        return

    # Conversation history
    history = []

    while True:

        # 1-Get user input
        try:
            user_input = get_user_input()

        except KeyboardInterrupt:
            print("\n\nChatbot stopped. Goodbye!")
            break

        except EOFError:
            print("\n\nInput ended. Goodbye!")
            break

        # 2-Check exit command
        if is_exit_command(user_input):
            print("Goodbye")
            break

        # 3-Validate input
        if is_empty_input(user_input):
            print("Please enter a message.\n")
            continue

        # 4-Build prompt 
        messages = build_messages(
            history,
            user_input
        )

        # 5-Call AI API
        try:
            response = get_ai_response(client,messages)

        # 6-Handle interruption during API request
        except KeyboardInterrupt:
            print("\n\nRequest interrupted. Returning to chatbot.")
            continue

        # 7-Handle API errors
        except Exception as e:
            print(f"\nError: {get_error_message(e)}\n")
            continue

        # 8-Process response
        reply = get_reply(response)

        # 9-Display response
        display_response(reply)

        # 10-Store conversation history
        history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        print()