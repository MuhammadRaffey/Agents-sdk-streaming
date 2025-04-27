from agents import Agent,Runner,RunConfig,OpenAIChatCompletionsModel,AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl # for UI
import os
from dotenv import load_dotenv, find_dotenv
import asyncio


_=load_dotenv(find_dotenv())

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set.")

client=AsyncOpenAI(api_key=groq_api_key, 
                  base_url="https://api.groq.com/openai/v1", )

model=OpenAIChatCompletionsModel(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    openai_client=client
)

config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)
agent1=Agent(
    name="Raffey's Agent",
    instructions="You are a helpful assistant and You respond in very well written markdown format.",
)

# Streaming 
# async def main():
#     agent = Agent(
#         name="Joker",
#         instructions="You are a helpful assistant.",

#     )
#     result=  Runner.run_streamed(agent1,input="Tell me Some Jokes on Noobs in PUBG",run_config=config)
#     # print(result.final_output)
#     async for event in result.stream_events():
#         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#             print(event.data.delta, end="", flush=True)

# asyncio.run(main())

# # Chainlit Integration for Sync
# @cl.on_chat_start
# async def handle_chat_start():
#     cl.user_session.set("histroy", [])
#     await cl.Message(content="Hello! I am your assistant created by Raffey.").send()

# @cl.on_message
# async def handle_message(message: cl.Message):
#     history=cl.user_session.get("histroy")
#     history.append({
#         "role": "user",
#         "content": message.content
#     })
#     result= await Runner.run(agent1,
#         input=history,
#         run_config=config)
#     history.append({
#         "role": "assistant",
#         "content": result.final_output
#     })
#     cl.user_session.set("histroy", history)
#     await cl.Message(content=result.final_output).send()

# # Chainlit Integration for Async
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("histroy", [])
    await cl.Message(content="Hello! I am your assistant created by Raffey.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history=cl.user_session.get("histroy")
    
    msg=cl.Message(content="")
    # await msg.send()

    history.append({
        "role": "user",
        "content": message.content
    })
    result=Runner.run_streamed(
        agent1,
        input=history,
        run_config=config)
    async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                token = event.data.delta
                await msg.stream_token(token)
    history.append({
        "role": "assistant",
        "content": result.final_output
    })
    cl.user_session.set("histroy", history)
    