from app.core.chunking import PdfChunker
from app.core.embedding import DocumentEmbedder
from app.core.vectorDb import SetVectorDb
from app.core.retriever import Retriever
from app.core.vector_store import VectorStore
from app.core.rag import Rag
from app.core.save_docx import Save_Dcoument
from app.core.accuracy_measure import Accureacy
import time

if __name__ == "__main__":
    
    file_path = r"D:\DataScience\Assignments\Rag_Project\app\resources\LB_Finance.pdf"
    chunk_size = 500
    chunk_overlap = 50
    chunking_pdf = PdfChunker(file_path, chunk_size, chunk_overlap)
    pages = chunking_pdf.load_pdf()
    split_docs = chunking_pdf.chunk_pdf(pages) # These split docs are document type

    embed = DocumentEmbedder()
    #list of strings (page_content) not Documents
    #embed_docs = embed.embed_documents([doc.page_content for doc in split_docs])

    # Embedding the query
    #embed_query = embed.embed_query("Hi Hiroshi How are you")
    #print(len(embed_query)) 
    
    vector_db = SetVectorDb(reset=False)

    # Insert documents to Milvus
    VectorStore_ = VectorStore().vect_store

    retriever_ = {}
    retriever2_ = {}
    rag = {}
    response = {}

    # This code is without Ranking the documents and sending the retriever to the RAG.

    # When using a retriever, this is what happens inside the Rag pipeline:

        #User asks a question (e.g., "What are the financial improvements?")

        #Retriever fetches relevant documents from a vector store.

        #Those documents are sent to the LLM (via a prompt).

        #LLM gives an answer using those documents as context.

    query="can you compare and provide me all the financial figures have improved over the years"

    for name, store in VectorStore_.items():

        # Without Ranking... Following are the results

        store.add_texts(
            texts=[doc.page_content for doc in split_docs],  # texts are strings
            metadatas=[doc.metadata for doc in split_docs]
        )
        retriever_obj = Retriever(store)
        retriever_[name] = retriever_obj.get_retriever()
        retrieved_docs = retriever_[name].invoke(query)   # Retrieves document type objects - [Document(metadata={'moddate': '2024-06-04T18:40:33+05:30', 'trapped': '/False'


        average_similarity=Accureacy(query,retrieved_docs).average_similarity # This method is to measure the accuracy between retrieved and query
        print(f"Average similarity for index {name} before ranking: {average_similarity:.4f}")

        print("###########################################################################################")

        retriever2_[name] = retriever_obj.get_mmr_retriever()
        retrieved_docs2 = retriever2_[name].invoke(query)   # Retrieves document type objects - [Document(metadata={'moddate': '2024-06-04T18:40:33+05:30', 'trapped': '/False'


        average_similarity2=Accureacy(query,retrieved_docs2).average_similarity # This method is to measure the accuracy between retrieved and query
        print(f"Average similarity for index {name} after ranking: {average_similarity2:.4f}")


        rag[name] = Rag(retriever2_[name])

        start_time=time.time()
        response[name] = rag[name].invoke(query)

        end_time=time.time()


        print(f" Retrieval time for {name}: {end_time - start_time:.4f} seconds")

        print(f"Response for store {name}: {response[name]}")

        # Save the content in docx
        #Save_Dcoument().save_response_to_docx(response[name])

        
    saver = Save_Dcoument()
    for name, text in response.items():
        saver.save_response_to_docx(f"{name} Index Response", text)
    