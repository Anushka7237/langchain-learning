from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt
template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
# 2d prompt
template2=PromptTemplate(
    template='Write 5 line summary on the following text /n {text}',
    input_variables=['text']
)

# prompt1=template1.invoke({'topic':'Black hole'})
# result=model.invoke(prompt1)
# prompt2=template2.invoke({'text':result.content})
# final_result=model.invoke(prompt2)
# print(final_result.content)


parser=StrOutputParser()
chain=template1 | model | parser | template2 | model | parser
result=chain.invoke({'topic':'Black Hole'})
print(result)