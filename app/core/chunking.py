from langchain_community.document_loaders import  PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class PdfChunker:

    """Loads a PDF and splits it into chunks using LangChain tools."""

    def __init__(self,file_path,chunk_size,chunk_overlap):
        self.file_path=file_path
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap

    def load_pdf(self) -> list:
        loader=PyPDFLoader(self.file_path)
        pages=loader.load()
        return pages

    def chunk_pdf(self,pages)-> list:
        splitter=RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

        split_docs=splitter.split_documents(pages)
        return split_docs

