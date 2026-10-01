from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
import streamlit as st

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task='text-generatiom'
)

model=ChatHuggingFace(llm=llm)

chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input=input('You...')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    res=model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print("AI :",res.content)

print(chat_history)
