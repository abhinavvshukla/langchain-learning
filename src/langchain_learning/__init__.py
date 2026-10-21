from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatOllama(model="llama3.1:8b", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from langchain-learning!")
    agent_response = agent.invoke(
        {"messages": [HumanMessage(content="What is the current weather in Tokyo?")]}
    )
    print(agent_response["messages"][-1].content)