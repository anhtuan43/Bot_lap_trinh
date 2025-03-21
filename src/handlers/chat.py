from datetime import datetime
import chainlit as cl
from config import REFLECTION
from services import generate_response
from prompt import AITutorPrompt

async def start_chat():
    """Initialize chat history in the session."""
    cl.user_session.set("history", [])

async def handle_message(message: cl.Message):
    """
    Process the user's message and return a response from the LLM.
    
    Args:
        message (cl.Message): The user's message.
    """
    start_time = datetime.now()
    query = message.content

    # Retrieve and update chat history
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": query})

    # Generate a prompt from the most recent chat history
    latest_history = REFLECTION(history, lastItemsConsidereds=8)
    prompt = AITutorPrompt(history=latest_history).format()

    # Create an empty message for streaming
    msg = cl.Message(content="")
    await msg.send()

    # Call the LLM API and stream the response
    stream = generate_response(prompt)
    response_text = ""

    for event in stream:
        if event.choices[0].text:
            response_text += event.choices[0].text
            await msg.stream_token(event.choices[0].text)

    # Update chat history with the response
    history.append({"role": "Assistant", "content": response_text})
    cl.user_session.set("history", history)

    # Calculate processing time and update the message
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()
    final_content = f"{response_text} (⏱ {processing_time:.3f}s)"
    msg.content = final_content
    await msg.update()
