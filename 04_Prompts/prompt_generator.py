from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template = """
    You are an expert teacher.

    Explain the following topic in a simple and clear way.

    Subject: {subject_input}
    Topic: {topic_input}

    Provide:
    1. A simple definition
    2. Detailed explanation
    3. A practical example
    4. Important points to remember
    5. A short summary
    """,
    input_variables=['subject_input','topic_input']
)

template.save('template.json')