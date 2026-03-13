# IntelliDocs RAG Analyzer 🔍

IntelliDocs is an advanced Retrieval-Augmented Generation (RAG) system designed for high-precision analysis of complex documents, such as financial reports, legal contracts, and technical manuals. It provides accurate answers with direct source citations to ensure reliability and transparency.

## 🌟 Key Features

- **Hybrid Search**: Combines semantic search (vector-based) with keyword search (BM25) for superior retrieval accuracy.
- **Source Attribution**: Automatically cites specific pages and sections from the source documents in its answers.
- **Multi-Format Support**: Ingests PDF, DOCX, and Markdown files with advanced layout-aware parsing.
- **Agentic Re-ranking**: Uses a Cross-Encoder model to re-rank retrieved chunks for the highest relevance.
- **Streamlit UI**: Includes a clean, interactive dashboard for document uploading and querying.

## 🛠️ Tech Stack

- **Core**: Python 3.10+
- **RAG Framework**: LangChain / LlamaIndex
- **Vector Database**: ChromaDB / Pinecone
- **Embeddings**: OpenAI `text-embedding-3-small` / HuggingFace
- **LLM**: OpenAI GPT-4o-mini / Anthropic Claude 3.5 Haiku
- **Frontend**: Streamlit

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/TalhaJabbarr/IntelliDocs-RAG-Analyzer.git
   cd IntelliDocs-RAG-Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment**
   ```bash
   cp .env.example .env
   # Add your API keys (OPENAI_API_KEY, etc.)
   ```

4. **Launch the Analyzer**
   ```bash
   streamlit run app.py
   ```

## 📂 Repository Structure

```text
├── data/                # Sample documents for testing
├── src/
│   ├── ingestion/       # Document parsing and vectorization logic
│   ├── retrieval/       # Hybrid search and re-ranking algorithms
│   ├── chains/          # RAG pipeline definitions
│   └── utils/           # Helper functions for processing
├── app.py               # Streamlit application entry point
├── requirements.txt
└── README.md
```

## 🤝 Contributing

We welcome contributions! Please open an issue or submit a PR for any improvements.

---
Developed with ❤️ by [Talha Jabbar](https://www.linkedin.com/in/talha-jabbar-067ba6203/)
