from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following --{question} from the /n {text}',
    input_variables=['question','text']
)

parser=StrOutputParser()

url="https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdhe4hn-a/p/itm8505e2f874525"
loader=WebBaseLoader(url)
docs=loader.load()

chain=prompt|model|parser
final_res=chain.invoke({'question':'What is price of Apple MacBook Air (M5, 2026)','text':docs[0].page_content})

print(final_res)