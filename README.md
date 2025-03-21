# AI Tutor - Chatbot using Chainlit and LLM

## Overview
AI Tutor is a chatbot built using **Chainlit**, integrating a **Large Language Model (LLM)** to provide interactive tutoring experiences. The system leverages **OAuth authentication**, maintains chat history, and generates responses based on user inputs.

## Features
- **Interactive Chat**: Users can engage in real-time conversations with AI Tutor.
- **Chat History**: The chatbot maintains a session-based conversation history.
- **LLM Integration**: Uses a configurable language model (default: `LLama-3.3-70B-Instruct`).
- **OAuth Authentication**: Supports authentication via Google.
- **Streaming Responses**: Responses are streamed progressively for a smoother user experience.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Virtual environment (optional but recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-tutor.git
   cd ai-tutor
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```sh
   export api_key_fpt="your-api-key"
   export api_url_fpt="your-api-url"
   ```
   (For Windows PowerShell: `Set-Item -Path env:api_key_fpt -Value "your-api-key"`)

## Usage
### Start the Chatbot
Run the chatbot using:
```sh
chainlit run main.py
```

### OAuth Authentication
The chatbot supports Google OAuth authentication via the following function:
```python
def oauth_callback(provider_id: str, token: str, raw_user_data: Dict[str, str], default_user: cl.User) -> Optional[cl.User]:
    """OAuth authentication with Google."""
    if provider_id == "google":
        return cl.User(
            identifier=raw_user_data["email"],
            metadata={"provider": "google", "name": raw_user_data.get("name", "")}
        )
    return None
```

### Handling Messages
The chatbot processes messages through the `handle_message` function:
```python
async def handle_message(message: cl.Message):
    """Processes user messages and returns LLM-generated responses."""
    start_time = datetime.now()
    query = message.content
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": query})
    latest_history = REFLECTION(history, lastItemsConsidereds=8)
    prompt = AITutorPrompt(history=latest_history).format()
    msg = cl.Message(content="")
    await msg.send()
    stream = generate_response(prompt)
    response_text = ""
    for event in stream:
        if event.choices[0].text:
            response_text += event.choices[0].text
            await msg.stream_token(event.choices[0].text)
    history.append({"role": "Assistant", "content": response_text})
    cl.user_session.set("history", history)
    processing_time = (datetime.now() - start_time).total_seconds()
    msg.content = f"{response_text} (⏱ {processing_time:.3f}s)"
    await msg.update()
```

## Configuration
- `config.py`: Contains API keys, model configuration, and other settings.
- `services.py`: Handles API calls to generate responses.
- `prompt.py`: Manages prompt formatting.

## Customization
- Modify `DEFAULT_MODEL` and `MAX_TOKENS` in `config.py` to change the model settings.
- Adjust `lastItemsConsidereds` in `handle_message` to tweak the number of past messages considered for response generation.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests! 🚀

