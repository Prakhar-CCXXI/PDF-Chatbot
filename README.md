# PDF-CHATBOT USING OLLAMA AND RAG

```markdown
# 📄 PDF Chatbot — Retrieval Augmented Generation (RAG)

A **Retrieval Augmented Generation (RAG) chatbot** that allows users to upload PDF documents and ask natural language questions based on their content.  
The system uses **semantic search with FAISS**, **local LLM inference using Ollama**, and a **Streamlit-based user interface** to generate context-aware responses grounded in the uploaded document.

---

## 🚀 Features

- 📄 Upload and query PDF documents
- 🧠 Context-aware answers using RAG architecture
- 🔍 Semantic search using FAISS vector database
- 🤖 Local LLM inference (no external API dependency)
- 🧩 Modular and extensible Python codebase
- 🎯 Designed for learning and experimentation with GenAI systems

---

## 🧠 Architecture Overview

```

User (Browser)
|
▼
Streamlit UI
|
▼
Text Chunking & Embeddings
|
▼
FAISS Vector Store
|
▼
LLM (Ollama - llama3.2)

```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| UI | Streamlit |
| LLM | Ollama (llama3.2) |
| Embeddings | Sentence-Transformers |
| Vector DB | FAISS |
| RAG Framework | LangChain |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```

PDF-Chatbot/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md

````

---

## ⚙️ Prerequisites

- Python 3.10+
- Ollama installed locally
- At least **8 GB RAM** recommended
- Linux / macOS / WSL

---

## ▶️ Running the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Prakhar-CCXXI/PDF-Chatbot.git
cd PDF-Chatbot
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Pull the LLM Model

```bash
ollama pull llama3.2
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 How It Works

1. User uploads a PDF document
2. Text is extracted from the PDF
3. Text is split into overlapping chunks
4. Chunks are embedded using sentence-transformers
5. FAISS stores and retrieves relevant chunks
6. The LLM generates answers using retrieved context

---

## ⚠️ Challenges Faced & Solutions

### 1️⃣ LangChain Breaking Changes

**Challenge:**
Frequent breaking changes in LangChain caused import errors and deprecated APIs, especially for text splitters and retrieval chains.

**Solution:**

* Migrated to modular packages like `langchain-community` and `langchain-text-splitters`
* Used stable APIs such as `RetrievalQA.from_chain_type`
* Pinned compatible versions in `requirements.txt`

---

### 2️⃣ Python 3.12 Compatibility Issues

**Challenge:**
Several tutorials relied on deprecated libraries (`PyPDF2`) that failed under Python 3.12.

**Solution:**

* Replaced `PyPDF2` with `pypdf`
* Updated imports to ensure compatibility with modern Python versions

---

### 3️⃣ Understanding RAG Pipeline Design

**Challenge:**
Designing the end-to-end RAG pipeline required understanding how chunking, embeddings, retrieval, and generation interact.

**Solution:**

* Studied the flow of data across each stage
* Tuned chunk size and overlap for better context retention
* Validated retrieval quality before passing context to the LLM

---

### 4️⃣ Local LLM Resource Constraints

**Challenge:**
Running LLMs locally required careful consideration of system memory and performance.

**Solution:**

* Selected lightweight models suitable for CPU inference
* Optimized prompt size by limiting retrieved context
* Avoided unnecessary re-embedding of documents

---

### 5️⃣ Git & Version Control Issues

**Challenge:**
Initial GitHub integration resulted in merge conflicts and unrelated history errors.

**Solution:**

* Learned to resolve merge conflicts manually
* Used `.gitignore` to exclude generated and environment-specific files
* Followed proper Git workflows for syncing local and remote repositories

---

## 🔐 Important Notes

* LLM models are **not committed to GitHub**
* FAISS indexes are generated at runtime
* Uploaded PDFs are excluded from version control
* `.gitignore` ensures a clean and lightweight repository

---

## 📌 Future Enhancements

* Multi-PDF ingestion
* Chat history memory
* Improved UI/UX
* Authentication & user sessions
* GPU acceleration
* Cloud deployment support

---

## 👨‍💻 Author

**Prakhar Jaiswal**
GitHub: [https://github.com/Prakhar-CCXXI](https://github.com/Prakhar-CCXXI)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

````

---

## ✅ Final Commit Command

```bash
git add README.md
git commit -m "Update README with challenges faced (non-Docker)"
git push origin main
````

---

### 🎯 Why This Version Is Strong

* No Docker noise (as requested)
* Shows **problem-solving & learning**
* Honest challenges (very recruiter-friendly)
* Clear GenAI & RAG understanding
* Perfect for **fresher + internship + entry-level roles**

