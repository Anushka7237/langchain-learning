from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

llm1=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)
llm2=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
llm3=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model1=ChatHuggingFace(llm=llm1)
model2=ChatHuggingFace(llm=llm2)
model3=ChatHuggingFace(llm=llm3)

prompt1=PromptTemplate(
    template='generate a short and simple notes about the {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='generate 2 question answer about the following {text}',
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes->{notes} quiz->{quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()
notes_chain = prompt1 | model1 | parser
quiz_chain = prompt2 | model2 | parser
parallel_chain = RunnableParallel({
    "notes": notes_chain,
    "quiz": notes_chain | quiz_chain
})

merge_chain= prompt3 | model3 |parser
chain=parallel_chain|merge_chain
result=chain.invoke({'topic':'Data Science'})
print(result)