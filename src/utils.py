import re

#clean unnecessary data
def clean_input(text):
    if not isinstance(text, str):
        return ""

    # Remove whitespaces
    text = text.strip()

    # Replace multiple whitespace characters with one space
    text = re.sub(r"\s+", " ", text)

    return text

#checks empty inputs
def is_empty_input(text):
    return not text.strip()

#exit command
def is_exit_command(text):
    exit_commands = {
        "exit",
        "quit",
        "bye"
    }

    return text.lower() in exit_commands

#get reply from ai response
def get_reply(response):
    try:
        text = response.choices[0].message.content

        if not text:
            return (
                "Sorry, I received an empty response. "
                "Please try again."
            )

        return text.strip()

    except (AttributeError, IndexError, TypeError):
        return (
            "Sorry, I could not process the AI response."
        )

#in case of error detected
def get_error_message(error):
    error_text = str(error).lower()

    if "401" in error_text or "unauthorized" in error_text:
        return (
            "Authentication failed. "
            "Please check your Hugging Face token."
        )

    if "429" in error_text or "rate limit" in error_text:
        return (
            "The API rate limit has been reached. "
            "Please wait and try again."
        )

    if "timeout" in error_text:
        return (
            "The AI service took too long to respond. "
            "Please try again."
        )

    if "connection" in error_text:
        return (
            "Could not connect to the AI service. "
            "Please check your internet connection."
        )

    if "503" in error_text or "unavailable" in error_text:
        return (
            "The AI model is currently unavailable. "
            "Please try again later."
        )

    return (
        "Sorry, something went wrong while contacting "
        "the AI service. Please try again."
    )