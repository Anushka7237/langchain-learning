from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='generate a detailed report about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='generate 5 line summary from the following text \n {text}',
    input_variables=['text']
)

chain= prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({'topic':'DataScienc'})
# print(result)

chain.get_graph().print_ascii()