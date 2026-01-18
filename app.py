import os
import streamlit as st
from PyPDF2 import PdfReader

# ✅ LangChain (latest structure)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

# LCEL
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# -----------------------------
# Helper Functions
# -----------------------------

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def create_vector_store(text, index_path="faiss_index"):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local(index_path)


def load_vector_store(index_path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )


def build_rag_chain(index_path="faiss_index"):
    vectorstore = load_vector_store(index_path)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


    
    prompt = PromptTemplate.from_template(
        """Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}
"""
    )

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("📄 RAG Chatbot (FAISS + LLaMA)")
st.write("Upload a PDF and ask questions based on its content.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    os.makedirs("uploaded", exist_ok=True)
    pdf_path = os.path.join("uploaded", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("📖 Reading PDF..."):
        text = extract_text_from_pdf(pdf_path)

    with st.spinner("🧠 Creating vector store..."):
        create_vector_store(text)

    with st.spinner("🤖 Initializing chatbot..."):
        st.session_state.rag_chain = build_rag_chain()

    st.success("✅ Chatbot is ready!")


if "rag_chain" in st.session_state:
    question = st.text_input("Ask a question")

    if question:
        with st.spinner("🔍 Thinking..."):
            answer = st.session_state.rag_chain.invoke(question)

        st.markdown("### 💡 Answer")
        st.write(answer)
