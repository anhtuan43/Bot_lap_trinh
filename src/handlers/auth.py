import chainlit as cl
from typing import Dict, Optional

def oauth_callback(provider_id: str, token: str, raw_user_data: Dict[str, str], default_user: cl.User) -> Optional[cl.User]:
    """OAuth authentication with Google."""
    if provider_id == "google":
        return cl.User(
            identifier=raw_user_data["email"],
            metadata={"provider": "google", "name": raw_user_data.get("name", "")}
        )
    return None
