from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7
)

prompt=PromptTemplate(
    template='Write a summary about the poem --\n{poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

loader=TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content}))
