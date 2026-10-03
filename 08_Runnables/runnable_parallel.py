from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Generate about the {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a linkedin post about {topic}',
    input_variables=['topic']
)

chain=RunnableParallel({
    'tweets':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

result=chain.invoke({'topic':'AI'})
print(result)


# <-------------------------What the code does----------------------------------->
# Takes a topic as input.
# Sends the same topic to two separate chains in parallel:
# tweets → generates content about the topic.
# linkedin → generates a LinkedIn post about the topic.
# Returns both outputs together in a dictionary.