# Import the OpenAI library to interact with the OpenAI API
from openai import OpenAI

# Import configuration variables from the config file
from config import API_KEY, GEN_API_URL, DEFAULT_MODEL, MAX_TOKENS

def generate_response(prompt: str, model: str = DEFAULT_MODEL, max_tokens: int = MAX_TOKENS, api_key: str = API_KEY, url: str = GEN_API_URL):
    """
    This function sends a request to the OpenAI API to generate a response based on the input prompt.

    Parameters:
    - prompt (str): The input question or text for which a response is needed.
    - model (str): The AI model used for generating the response (default is taken from config).
    - max_tokens (int): The maximum number of tokens for the response (default is taken from config).
    - api_key (str): The API key for authentication with OpenAI (default is taken from config).
    - url (str): The OpenAI API URL (default is taken from config).

    Returns:
    - stream: A response stream generated by the API.
    """

    # Initialize the OpenAI client with the API URL and API key
    client = OpenAI(
        base_url=url,
        api_key=api_key
    )

    # Send a request to generate a response using the specified model, prompt, and max tokens
    stream = client.completions.create(
        model=model,
        prompt=prompt,
        stream=True,  # Enable streaming mode to receive the response gradually
        max_tokens=max_tokens
    )

    return stream  # Return the response stream from the API
