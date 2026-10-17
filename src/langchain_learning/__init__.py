from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello from langchain-learning!")
    prompt = PromptTemplate(
        template="Say {foo} to {bar}, with a smile.",
        input_variables=["foo", "bar"]
    )
    llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = prompt | llm
    response = chain.invoke(input={"foo": "hi","bar": "abhi"})
    print(response.content)