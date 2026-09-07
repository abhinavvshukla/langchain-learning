from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("Your OpenAI API Key is:", api_key)  

if __name__ == "__main__": 
    main()