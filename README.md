# 🔍 RAG Chatbot using LLaMA 3 + FAISS

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDFs and ask context-aware questions using **LLaMA 3 via Ollama**, **LangChain**, and **FAISS**.

---

## 🚀 Features
- Upload PDF documents
- Semantic search using FAISS
- Context-aware responses using LLaMA 3
- Dockerized deployment
- Nginx reverse proxy
- Runs fully locally (no external API calls)

---

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- Ollama (LLaMA 3)
- Docker & Docker Compose
- Nginx
- AWS EC2 (Deployment)

---

## 🧠 Architecture
1. PDF uploaded via Streamlit UI
2. Text extraction & chunking
3. Embeddings using sentence-transformers
4. FAISS vector store
5. LLaMA 3 generates answers using retrieved context

---

## ⚙️ Setup Instructions

### 1. Install Ollama
```bash
ollama pull llama3.2
