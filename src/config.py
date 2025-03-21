import os
from dotenv import load_dotenv
from reflection import Reflection

load_dotenv()

# API Configuration
API_KEY = os.getenv("api_key_fpt")
GEN_API_URL = os.getenv("api_url_fpt")

# Initialize reflection
REFLECTION = Reflection()

# Model Configuration
DEFAULT_MODEL = "LLama-3.3-70B-Instruct"
MAX_TOKENS = 800
