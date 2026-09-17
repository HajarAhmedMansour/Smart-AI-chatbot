import os
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# Get the project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the .env file from the project root
env_path = BASE_DIR / ".env"

loaded = load_dotenv(env_path)

HF_TOKEN = os.getenv("HF_TOKEN")
print("Token loaded:", HF_TOKEN is not None)


# Hugging Face model
MODEL_NAME = "Qwen/Qwen3-4B-Instruct-2507"


def create_client():
    if not HF_TOKEN:
        raise ValueError(
            "Hugging Face API token is missing. "
            "Check your .env file."
        )

    return InferenceClient(
        model=MODEL_NAME,
        api_key=HF_TOKEN,
        provider="auto"
    )

def get_ai_response(client, messages):
    try:
        response = client.chat_completion(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=1500,
            top_p=0.9,
            temperature=0.7
        )

        return response

    except Exception as e:
        print(f"API Error: {e}")

        return None

