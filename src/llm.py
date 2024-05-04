import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(user_message,instruction):

    llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    response=llm([SystemMessage(content=instruction),HumanMessage(content=user_message)])   
    return response.content

    '''
    messages=[{"role": "system", "content":instruction }, {"role": "user", "content": user_message}]  
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    response = llm.invoke(messages)
    '''
    

'''
if __name__ == "__main__":
    print("Welcome to chat bot!")
    user_message = "Hi, How are you?"
    response=ask_bot("What is the meaning of large language models?")
    print(response.content)

    #message=ask_bot("What is the meaning of large language models?")
    #print(message)
'''
    
    
