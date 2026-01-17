# 05 - Q&A Generation

## Purpose
Integrate LLM with retrieval to generate cited, synthesized answers.

## Notebooks
- `llm_integration.ipynb` - Set up Gemini API
- `rag_pipeline.ipynb` - Build end-to-end RAG system
- `answer_grading.ipynb` - Evaluate answer quality

## Outputs
- `qa_pairs_validation/` - Ground truth Q&A for testing

## Key Features
- Prompt engineering for medical Q&A
- Citation extraction from retrieved chunks
- Answer synthesis (not regurgitation)
- Faithfulness and relevance metrics
