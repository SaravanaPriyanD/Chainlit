import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

message=[{"role": "system", "content":instruction}]

def ask_bot(message):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    response = llm.invoke(message)
    return response.content

if __name__ == "__main__":
    print("Welcome to chat bot!")
    message=ask_bot("What is the meaning of large language models?")
    print(message)


