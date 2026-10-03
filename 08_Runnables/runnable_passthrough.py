from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough

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

joke_generator=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_generator,parallel_chain)

result=final_chain.invoke({'topic':'AI'})
print(result)



# <------------------------What the code does---------------------------------->
# Takes a topic as input.
# Generates a joke using the LLM.
# Passes the generated joke to RunnableParallel.
# In parallel:
# RunnablePassthrough() → returns the original joke.
# prompt2 → model → parser → generates an explanation of the joke.
# Returns both the joke and its explanation.