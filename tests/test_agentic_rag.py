import unittest
from rag_engine.eval.ragas_metrics import RAGASEvaluator
from rag_engine.workflow import AgenticRAGWorkflow


class TestAgenticRAG(unittest.TestCase):
    def setUp(self):
        self.workflow = AgenticRAGWorkflow()

    def test_end_to_end_agentic_generation(self):
        query = "How does pgvector optimize vector indexing?"
        result = self.workflow.execute(query)

        self.assertTrue(result["grounded"])
        self.assertIn("citations", result)
        self.assertGreaterEqual(len(result["citations"]), 1)
        self.assertIn("pgvector", result["answer"].lower())

    def test_ragas_evaluation_metrics(self):
        answer = "pgvector provides HNSW and IVFFlat indexing in PostgreSQL."
        context = ["pgvector provides HNSW and IVFFlat indexing."]
        metrics = RAGASEvaluator.evaluate(answer, context, ground_truth=answer)

        self.assertGreaterEqual(metrics["faithfulness"], 0.60)
        self.assertGreaterEqual(metrics["context_precision"], 0.80)


if __name__ == "__main__":
    unittest.main()
