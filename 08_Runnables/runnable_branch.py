from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnableLambda,RunnablePassthrough

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Write a detailed report on this {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Summary the following {text}',
    input_variables=['text']
)

def word_count(text):
    return len(text.split())

report_generation=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:word_count(x)>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_generation,branch_chain)
result=final_chain.invoke({'topic':'Ai'})
print(result)


# <--------------- What the code does------------>
# Takes a topic as input.
# Generates a detailed report using the LLM.
# Counts the number of words in the generated report.
# If the report has more than 500 words, it generates a summary.
# If it has 500 words or fewer, it returns the original report.