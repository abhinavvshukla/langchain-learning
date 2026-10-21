from typing import List 
from pydantic import BaseModel, Field, Json   
from langchain.agents.structured_output import ToolStrategy

from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient 
import json

load_dotenv()

tavily = TavilyClient()

class Source(BaseModel):
    """Schema for source used by base model."""
    url: str = Field(description="The URL of the source.")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources."""
    answer: str = Field(description="agent's answer to the query.")
    sources: List[Source] = Field(default_factory=list, description="A list of sources used by the agent to generate the answer.")

@tool
def search(query: str) -> str:
    """Search for information using Tavily
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    print(f"Searching for: {query}")
    return json.dumps(tavily.search(query = query))

llm = ChatOllama(model="llama3.1:8b", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools, response_format=ToolStrategy(AgentResponse))

def main() -> None:
    print("Hello from langchain-learning!")
    agent_response = agent.invoke(
        {"messages": [HumanMessage(content="What is the current weather in Tokyo?")]}
    )
    print(agent_response)