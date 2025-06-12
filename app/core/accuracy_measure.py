import nltk
from nltk.corpus import stopwords
from app.core.embedding import DocumentEmbedder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Accureacy:
    '''This class is to calculate the Average Cosine Similarity'''
    def __init__(self,query, retrieved_docs):
        embed=DocumentEmbedder()
        embed_query=embed.embed_query(query)
        embed_doc=embed.embed_documents([i.page_content for i in retrieved_docs])

        similarities = cosine_similarity([embed_query], embed_doc)
        self.average_similarity = np.mean(similarities)
