
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

class DocumentEmbedder:
    def __init__(self):
        load_dotenv()
        #self.embeddings = OpenAIEmbeddings(
        #    model="text-embedding-3-large",
        #)

        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

    def embed_documents(self, texts: list[str]):
        return self.embeddings.embed_documents(texts)

    def embed_query(self, my_query: str):
        return self.embeddings.embed_query(my_query)
