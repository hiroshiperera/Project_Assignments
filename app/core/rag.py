
from app.core.outPutParser import OutputParser
from app.core.prompt import Prompt
from app.core.llm import LLM
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class Rag:
    def __init__(self, retriever_):
        parser = StrOutputParser()
        self.rag_chain = (
            {
                "context": retriever_ | OutputParser().get_parser(),
                "question": RunnablePassthrough()
            }
            | Prompt().get_prompt()
            | LLM().get_llm()
            | parser
        )

    def invoke(self, question: str):
        return self.rag_chain.invoke(question)
