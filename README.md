# Smart AI Chatbot

An AI chatbot built with Python and the Hugging Face Inference API. The chatbot maintains conversation history so that the model can understand previous messages and respond with contextual answers.

## Features

* Interactive command-line chatbot
* Powered by a Hugging Face language model
* Maintains conversation history
* Uses a system prompt to control the assistant's behaviour
* Cleans and validates user input
* Supports `exit` command
* Handles authentication, connection, timeout, rate-limit, and API errors
* Securely loads the Hugging Face API token from a `.env` file
* Configurable generation parameters


## Project Structure

```text
Smart AI chatbot/
│
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
│
└── src/
    ├── api_client.py
    ├── chatbot.py
    ├── prompts.py
    └── utils.py
```

| File                | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| `main.py`           | Entry point for starting the chatbot                                |
| `src/chatbot.py`    | Handles the main chatbot loop and conversation flow                 |
| `src/api_client.py` | Loads the API token and communicates with Hugging Face              |
| `src/prompts.py`    | Defines the system prompt and builds model messages                 |
| `src/utils.py`      | Handles input cleaning, validation, response processing, and errors |
| `requirements.txt`  | Contains the required Python dependencies                           |
| `README.md`         | Project documentation                                               |

## Requirements

* Python 3.10 or newer
* Internet connection
* Hugging Face account
* Hugging Face API token

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/HajarAhmedMansour/Smart-AI-chatbot.git>
cd "Smart AI chatbot"
```

### 2. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure the Hugging Face API token

Create a `.env` file in the project root:

```text
HF_TOKEN=hf_your_token_here
```

Use your own Hugging Face API token.

**Do not commit the `.env` file or your API token to GitHub.**

## Running the Chatbot

From the project root, run:

```bash
python main.py
```

The chatbot will start in the terminal:

```text
Smart AI Chatbot
------------------------------
Type 'exit' to end the conversation.
```

You can then enter messages:

```text
You: What is Python?

Bot: Python is a high-level programming language...
```

To end the conversation, use:

```text
exit
```

The chatbot also accepts:

```text
quit
bye
```

## How It Works

The chatbot follows this general flow:

```text
User Input
    ↓
Input Cleaning
    ↓
Input Validation
    ↓
Conversation History
    ↓
System Prompt + Conversation + Current Message
    ↓
Hugging Face Inference API
    ↓
AI Response
    ↓
Response Processing
    ↓
Display Response
    ↓
Update Conversation History
```

### Conversation History

The chatbot stores previous user and assistant messages and sends them with the current request.

For example:

```python
[
    {
        "role": "user",
        "content": "What is Python?"
    },
    {
        "role": "assistant",
        "content": "Python is a programming language..."
    }
]
```

This allows the model to maintain context throughout the conversation.

### Prompt Construction

A system prompt defines the assistant's behaviour. The model receives:

```text
System Prompt
      ↓
Previous Conversation
      ↓
Current User Message
```

This helps maintain consistent behaviour and conversational context.

### AI Model

The chatbot currently uses:

```text
Qwen/Qwen3-4B-Instruct-2507
```

through the Hugging Face Inference API.

The generation parameters currently include:

```python
max_tokens=1500
temperature=0.7
top_p=0.9
```

* `max_tokens` controls the maximum length of the generated response.
* `temperature` controls the randomness of the generated response.
* `top_p` controls the range of tokens considered during generation.

These parameters can be adjusted in `src/api_client.py`.

## Error Handling

The chatbot handles several common API problems:

| Error                       | Response                                             |
| --------------------------- | ---------------------------------------------------- |
| Authentication / `401`      | Requests the user to check the API token             |
| Rate limit / `429`          | Informs the user that the API rate limit was reached |
| Timeout                     | Requests the user to try again                       |
| Connection error            | Suggests checking the internet connection            |
| Service unavailable / `503` | Suggests trying again later                          |
| Other errors                | Displays a general error message                     |

## Example Conversation

```text
Smart AI Chatbot
------------------------------
Type 'exit' to end the conversation.

You: What is machine learning?

Bot: Machine learning is a branch of artificial intelligence that
allows computers to learn patterns from data and use those patterns
to make predictions or decisions.

You: What are its main types?

Bot: The main types are supervised learning, unsupervised learning,
and reinforcement learning.

You: Give me an example of supervised learning.

Bot: A common example is email spam detection, where a model learns
from labelled examples of spam and non-spam emails.

You: bye

Goodbye
```

## Security

The Hugging Face API token is stored in a local `.env` file instead of being written directly in the Python source code.

The `.env` file should be included in `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

Never commit your API token to a public repository.

## Technologies Used

* Python
* Hugging Face Inference API
* Qwen3-4B-Instruct-2507
* `huggingface_hub`
* `python-dotenv`
