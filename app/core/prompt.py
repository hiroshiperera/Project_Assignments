from langchain_core.prompts import PromptTemplate

class Prompt:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            You are a financial analyst AI assistant. Use the below extracted text from an annual report to answer the user's question.

            Give **precise answers**. If the information is not directly available, try to infer it logically.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """
        )

    def get_prompt(self):
        return self.prompt
