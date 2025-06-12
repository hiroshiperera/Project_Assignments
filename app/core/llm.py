
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

class LLM:
    def __init__(self):
        load_dotenv()
        GEN_AI_KEY = os.getenv("GOOGLE_GEN_API_KEY")  # FIXED typo: `os.get` -> `os.getenv`
        self.model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEN_AI_KEY)

    def get_llm(self):
        return self.model