import os

from dotenv import load_dotenv
load_dotenv()

import json

import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

async def main():
    client = MultiServerMCPClient(
        {
            "clarity": {
                "command": "python",
                "args": ["clarity_server.py"],
                "transport": "stdio"
            },
            "ga": {
                "command": "python",
                "args": ["ga_server.py"],
                "transport": "stdio"
            },
            "logs": {
                "command": "python",
                "args": ["logs_server.py"],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.2)
    agent = create_react_agent(model=model, tools=tools)

    clarity_response = await agent.ainvoke(
        {"messages": [
            {"role": "user",
             "content": "Please provide clarity session summaries and filter out the data that is actually important and relevant for analysis."
            }
        ]
        }
    )
    clarity_response = next((msg for msg in clarity_response['messages'] if msg.type == "tool"), None)
    session_summaries = json.loads(clarity_response.content[0]['text'])

    ga_response = await agent.ainvoke(
        {"messages": [
            {"role": "user",
             "content": "Please provide google analytics data and filter out the data that is actually important and relevant for analysis."
            }
        ]
        }
    )

    ga_response = next((msg for msg in ga_response['messages'] if msg.type == "tool"), None)
    analytics = json.loads(ga_response.content[0]['text'])

    logs_data = await agent.ainvoke(
        {"messages": [
            {"role": "user",
             "content": "Please fetch the logs."
            }
        ]
        }
    )
    logs_data = next((msg for msg in logs_data['messages'] if msg.type == "tool"), None)
    logs = json.loads(logs_data.content[0]['text'])

    return session_summaries, analytics, logs
    # return logs

# session_summaries, analytics, logs = asyncio.run(main())