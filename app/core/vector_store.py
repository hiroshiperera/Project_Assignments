from langchain_milvus import Milvus
from app.core.index import Indexes
from app.core.vectorDb import SetVectorDb
from app.core.embedding import DocumentEmbedder

class VectorStore:
    def __init__(self):
        self.indexes_= Indexes().index_dict
        self.vect_store={}
        db_config = SetVectorDb()
        # Create vectorstore object using langchain_milvus
        for name,index_params in self.indexes_.items():
            self.vect_store[name] = Milvus(
                embedding_function=DocumentEmbedder(),
                connection_args={
                    "uri": "http://localhost:19530",
                    "token": "root:Milvus",   # Change if you use other credentials
                    "db_name": db_config.db_name,
                },
                index_params=index_params,  # list of index dicts
                consistency_level="Strong",
                drop_old=db_config.reset,
                search_params={"ef": 50, "metric_type": "L2"}, 
            )


    def get_store(self, name):
        return self.vect_store.get(name)


