from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Give a joke on {topic}',
    input_variables=['topic']
)

def word_count(text):
    return len(text.split())

start_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(start_chain,parallel_chain)
result=final_chain.invoke({'topic':'Girl'})
print(result)



# <-------------------------What the code does--------------------------------->
# Takes a topic as input.
# Generates a joke using the LLM.
# Sends the generated joke to two operations simultaneously:
# RunnablePassthrough() → keeps the original joke.
# RunnableLambda(word_count) → counts the words in the joke.
# Combines both results into a dictionary.