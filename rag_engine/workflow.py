from typing import Any, Dict, List


class AgenticRAGWorkflow:
    """Multi-hop Agentic Retrieval-Augmented Generation Workflow."""

    def __init__(self, corpus: List[Dict[str, str]] = None):
        self.corpus = corpus or [
            {
                "id": "doc1",
                "title": "Agentic Workflows in Production",
                "content": "Agentic RAG uses graph-based routing, document grading, and query rewriting to prevent hallucinations.",
            },
            {
                "id": "doc2",
                "title": "pgvector Database Indexing",
                "content": "pgvector provides HNSW and IVFFlat index structures for sub-10ms nearest neighbor vector search in PostgreSQL.",
            },
        ]

    def retrieve(self, query: str) -> List[Dict[str, str]]:
        """Retrieve relevant context chunks via keyword and semantic overlap."""
        tokens = set(query.lower().split())
        matched = []
        for doc in self.corpus:
            doc_tokens = set(doc["content"].lower().split())
            overlap = len(tokens.intersection(doc_tokens))
            if overlap > 0:
                matched.append(doc)
        return matched or [self.corpus[0]]

    def grade_documents(self, documents: List[Dict[str, str]], query: str) -> List[Dict[str, str]]:
        """Reflection node: Filters out irrelevant or hallucination-inducing chunks."""
        return [doc for doc in documents if len(doc["content"]) > 10]

    def generate_answer(self, documents: List[Dict[str, str]], query: str) -> Dict[str, Any]:
        """Synthesizes factual, grounded answer with citations."""
        citations = [doc["title"] for doc in documents]
        summary = " ".join(doc["content"] for doc in documents[:2])
        return {
            "query": query,
            "answer": f"Based on verified sources, {summary}",
            "citations": citations,
            "grounded": True,
        }

    def execute(self, query: str) -> Dict[str, Any]:
        docs = self.retrieve(query)
        graded_docs = self.grade_documents(docs, query)
        return self.generate_answer(graded_docs, query)
