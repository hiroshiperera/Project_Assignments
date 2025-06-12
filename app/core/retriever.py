from app.core.vectorDb import SetVectorDb

class Retriever:
    def __init__(self, vector_store):
        self.retriever=vector_store.as_retriever(
            search_kwargs={"k":5}
        )
        self.mmr_retriever=vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 5,
                "lambda_mult": 0.5,
            }
        )

    def get_retriever(self):
        return self.retriever
    

    def get_mmr_retriever(self):
        return self.mmr_retriever
    
