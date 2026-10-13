# 🧠 Enterprise Agentic RAG

[![CI Pipeline](https://github.com/MSBHOSLE/enterprise-agentic-rag/actions/workflows/ci.yml/badge.svg)](https://github.com/MSBHOSLE/enterprise-agentic-rag/actions)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Flows-FF6F00?logo=langchain&logoColor=white)](https://langchain.com/)
[![pgvector](https://img.shields.io/badge/PostgreSQL-pgvector-336791?logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-grade **Enterprise Agentic Retrieval-Augmented Generation (RAG)** platform. Utilizes **LangGraph** for autonomous routing, query rewriting, and self-reflective document grading with **pgvector** similarity retrieval and **RAGAS** hallucination/faithfulness evaluation metrics.

---

## 🏗️ Agentic Graph Workflow

```mermaid
flowchart TD
    Query(["User Query"]) --> Plan["Query Decomposer & Planner"]
    Plan --> Retrieve["pgvector Hybrid Similarity Retrieval"]
    Retrieve --> Grade{"Document Relevance Grading"}
    Grade -->|Relevant| Generate["Grounded Synthesis & Citations"]
    Grade -->|Insufficient| Rewrite["Agentic Query Transformation"]
    Rewrite --> Retrieve
    Generate --> Eval["RAGAS Faithfulness & Hallucination Check"]
    Eval --> Response(["Grounded Final Answer"])
```

---

## ⚡ Highlights

- **Reflective Document Grading**: Eliminates hallucination by actively grading chunk relevance before synthesis.
- **RAGAS Quality Gate**: Automated evaluation scoring Faithfulness, Answer Relevance, and Context Precision.
- **Hybrid Retrieval**: Combines semantic embeddings with dense vector index lookups.

---

## 🚀 Running Tests

```bash
python -m unittest discover tests
```

---

## 👤 Author

**Mahesh Sanjayrao Bhosle**
- **GitHub:** [@MSBHOSLE](https://github.com/MSBHOSLE)
- **LinkedIn:** [Mahesh Bhosle](https://linkedin.com/in/mahesh-bhosle-916991198)
- **Email:** msbhosle.2@gmail.com
- **Education:** M.Sc. Data & Computer Science, Heidelberg University

---

## 📄 License

MIT License - see [LICENSE](LICENSE).
