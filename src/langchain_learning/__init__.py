from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient 

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """Search for information using Tavily
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    print(f"Searching for: {query}")
    return tavily.search(query = query)

llm = ChatOllama(model="llama3.1:8b", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from langchain-learning!")
    agent_response = agent.invoke(
        {"messages": [HumanMessage(content="What is the current weather in Tokyo?")]}
    )
    print(agent_response.content)