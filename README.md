# 📄 Multi-Index RAG-based PDF Analyzer

A modular Retrieval-Augmented Generation (RAG) system for analyzing large, image-heavy PDFs using semantic chunking, vector search (FLAT, IVF, HNSW), reranking (MMR/BM25), LLM-based answering, and DOCX export. Built with LangChain, Milvus, FastAPI, and Streamlit.

---

## 🚀 Overview

This project extracts content from large PDFs (text, images, and tables), performs intelligent semantic chunking, and allows querying via multiple Milvus index types. It reranks results, generates LLM-powered responses (e.g., using Gemini/OpenAI), and writes them into a structured DOCX file.

---

## 🧠 Key Features

- ✅ **Semantic Chunking** with context-preserving logic
- ✅ **Multi-index support**: FLAT, IVF, HNSW (configurable)
- ✅ **Vector DB**: Milvus for fast approximate search
- ✅ **Reranking**: BM25 / MMR based relevance sorting
- ✅ **LLM Integration**: Gemini / OpenAI / Local
- ✅ **DOCX Export** of summarized answers
- ✅ **Modular codebase** with `core`, `api`, `frontend`, `services`, `tests`

---

## ⚙️ Project Structure

app/
│
├── api/ # FastAPI endpoints (To be done)
├── core/ # Core logic: chunking, embedding, indexing
├── frontend/ # Streamlit UI (To be done)
├── scripts/ # CLI or batch processors
├── services/ # RAG pipeline services
├── resources/ # PDFs and sample inputs
├── tests/ # Test cases
└── main.py # Entry point


---

## 📥 Installation

```bash
git clone https://github.com/yourname/rag-pdf-analyzer.git
cd rag-pdf-analyzer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
---
## 🛠️ Setup Milvus (Standalone)

docker-compose up -d  # Make sure milvus.yaml is present
---
## Run the App
---
# Backend API
uvicorn app.api.main:app --reload (To be done)
---
# Frontend (Optional)
streamlit run app/frontend/app.py

---
📊 Benchmarking
You can test:

🔹 Speed vs Accuracy per index (IVF vs HNSW vs FLAT)

🔹 Chunk size impact

🔹 Reranking effectiveness

📦 Output
output/combined_response.docx – Final LLM responses grouped by index
---
Logs and errors handled in logs/ (To be done)

🧩 Dependencies
        LangChain

        Milvus / pymilvus

        FastAPI

        Streamlit

        OpenAI / Gemini (optional)

        python-docx
---
🙌 Contributing
Pull requests welcome. For major changes, please open an issue first.
---