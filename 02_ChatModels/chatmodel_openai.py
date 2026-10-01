from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-5.6-luna",temperature=1.5,max_completion_tokens=10)

result=model.invoke("Write 4 lines hindi poem in hinglish")
print(result.content)