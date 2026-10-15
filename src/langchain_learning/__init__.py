from dotenv import load_dotenv
import os
load_dotenv()

def main() -> None:
    print("Hello from langchain-learning!")
    print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
