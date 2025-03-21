import chainlit as cl
from handlers import oauth_callback
from handlers import start_chat, handle_message

# Gắn OAuth callback
cl.oauth_callback(oauth_callback)

# Gắn sự kiện khởi động chat
cl.on_chat_start(start_chat)

# Gắn sự kiện xử lý tin nhắn
cl.on_message(handle_message)