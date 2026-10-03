from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Give me joke on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain the following joke -{text}',
    input_variables=['text']
)

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
result=chain.invoke({'topic':'Dancing girl'})
print(result)


# <----------------------------What the code does---------------------------->
# Takes a topic as input.
# prompt1 generates a joke about the topic.
# model generates the joke.
# parser converts the model output into a string.
# The generated joke is passed to prompt2.
# The model then explains the joke.
# The final parser returns the explanation.