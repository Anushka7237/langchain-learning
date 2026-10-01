from typing import TypedDict
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

class Student(TypedDict):
    name: str
    age: int
    branch: str

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

structured_model = model.with_structured_output(Student)

result = structured_model.invoke(
    "XYZ is 21 years old and studies Data Science."
)

print(result)