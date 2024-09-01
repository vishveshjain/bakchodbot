import chainlit as cl
from src.llm import bakchodi, messages


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message.content})
    response = bakchodi(messages)
    messages.append({"role": "assistant", "content": response})
    # Send a response back to the user
    await cl.Message(
        content=response
    ).send()
