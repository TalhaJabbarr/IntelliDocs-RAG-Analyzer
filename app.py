import streamlit as st
import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

st.set_page_config(page_title="IntelliDocs RAG Analyzer", page_icon="🔍")

st.title("🔍 IntelliDocs RAG Analyzer")
st.markdown("Upload documents and ask questions with precision and citations.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

uploaded_file = st.file_uploader("Upload a document (PDF)", type=["pdf"])

if uploaded_file and api_key:
    # Save file locally for processing
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Indexing document..."):
        # 1. Load and Split
        loader = PyPDFLoader("temp.pdf")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        
        # 2. Create Vector Store
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(texts, embeddings)
        
        # 3. Create RAG Chain
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
        )
        
        st.success("Document indexed successfully!")

    query = st.text_input("Ask a question about the document:")
    if query:
        with st.spinner("Searching for answers..."):
            result = qa_chain.invoke({"query": query})
            
            st.markdown("### 🤖 Answer:")
            st.write(result["result"])
            
            st.markdown("### 📄 Sources:")
            for doc in result["source_documents"]:
                st.info(f"Page {doc.metadata.get('page', 'Unknown')}: {doc.page_content[:200]}...")

elif not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar.")
