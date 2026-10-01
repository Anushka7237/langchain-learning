from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


st.header("Model")

subject_input = st.selectbox(
    "Select Subject Name",
    ["Data Science", "Machine Learning", "Python", "SQL", "Artificial Intelligence"]
)
topic_input = st.selectbox(
    "Select Topic",
    ["Basics", "Algorithms", "Projects", "Interview Questions", "Advanced Concepts"]
)

template=load_prompt(r'.\Langchain Prompts\template.json')




if st.button('Summarize'):
    chain=template|model
    res=chain.invoke({
    'subject_input':subject_input,
    'topic_input':topic_input
    }
    )
    st.write(res.content)