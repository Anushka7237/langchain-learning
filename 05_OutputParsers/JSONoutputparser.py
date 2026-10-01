from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser()
# 1st prompt
template1=PromptTemplate(
    template='give me age and city of frictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt=template1.format()
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
chain=template1 | model | parser
final_result=chain.invoke({})
print(final_result)