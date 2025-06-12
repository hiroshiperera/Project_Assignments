from app.core.embedding import DocumentEmbedder

class Indexes:
    def __init__(self):
        self.index_list=["FLAT","HNSW","IVF"]

        # Setup index params
        self.index_dict={}
        for index in self.index_list:
            self.index_dict[index] = self._get_index_params(index)


    def _get_index_params(self,index_type):

        dim = len(DocumentEmbedder().embed_query("test"))  # dynamically get dimension
        if index_type == "FLAT":
            return {
                "index_type": "FLAT",
                "metric_type": "L2",
                "params": {},
                "dim": dim
                }
        elif index_type == "IVF":
            return {
                "index_type": "IVF_FLAT",   # ✅ or IVF_SQ8, IVF_PQ etc.
                "metric_type": "L2",        # or "IP" (inner product)
                "params": {"nlist": 128},   # 🔹 Controls speed vs accuracy
                "dim": dim
            }
        elif index_type == "HNSW":
            return {
                "index_type": "HNSW",
                "metric_type": "L2",
                "params": {"M": 16, "efConstruction": 200},
                "dim": dim
            }
        else:
            raise ValueError(f"❌ Unsupported index type: {index_type}")
        
