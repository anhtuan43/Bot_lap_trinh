from openai import OpenAI
from config import API_KEY, GEN_API_URL, DEFAULT_MODEL, MAX_TOKENS

def generate_response(prompt: str, model: str = DEFAULT_MODEL, max_tokens: int = MAX_TOKENS, api_key: str = API_KEY, url: str = GEN_API_URL):
    client = OpenAI(
        base_url=url,
        api_key=api_key
    )

    stream = client.completions.create(
        model=model,
        prompt=prompt,
        stream=True,
        max_tokens=max_tokens
    )
    return stream