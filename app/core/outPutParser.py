from langchain_core.runnables import RunnableLambda

class OutputParser:
    def __init__(self):
        pass  # No need to initialize RunnablePassthrough

    @staticmethod
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def get_parser(self):
        return RunnableLambda(self.format_docs)