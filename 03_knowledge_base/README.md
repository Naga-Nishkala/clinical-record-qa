# 03 - Knowledge Base Construction

## Purpose
Convert clinical notes into embeddings and build patient-specific vector store.

## Notebooks
- `embedding_generation.ipynb` - Chunk notes and generate embeddings
- `vector_store_setup.ipynb` - Initialize ChromaDB with patient metadata

## Outputs
- `embeddings/` - Patient-specific embedding files
- `vector_store/` - ChromaDB database with patient_id filters
- `chunking_config.json` - Chunking strategy parameters

## Key Features
- Semantic chunking (preserves context)
- Patient_id metadata tagging
- Embedding model versioning
- Vector store configuration tracking
