from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def main() -> None:
    print("Hello from langchain-learning!")
    print("OPENAI_API_KEY configured:", bool(os.getenv("OPENAI_API_KEY")))

    prompt = PromptTemplate(
        template="Say {foo} to {bar}",
        input_variables=["foo", "bar"]
    )

    # print(prompt.format(foo="hello", bar="world"))

    llm = ChatOpenAI(model_name="gpt-5", temperature=0)
    # print(llm)
    chain = prompt | llm
    response = chain.invoke(input={"foo": "hello", "bar": "abhinav"})
    print(response)