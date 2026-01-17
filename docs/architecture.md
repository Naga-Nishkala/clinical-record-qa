# System Architecture

## Overview
The Clinical Notes Q&A System uses a Retrieval-Augmented Generation (RAG) architecture with strict patient data isolation.

## Architecture Diagram
```
┌─────────────────┐
│ Patient Query   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Patient ID Selection    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Vector Store Retrieval  │
│ (Filtered by patient_id)│
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Retrieved Chunks (Top-K)│
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ LLM Reasoning           │
│ (Gemini 2.0 Flash)      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Cited Answer            │
│ (with source notes)     │
└─────────────────────────┘
```

## Components

### 1. Data Layer
- **Synthetic Data**: Realistic clinical notes
- **De-identification**: PHI removal pipeline
- **Storage**: Google Drive (dev), GitHub (production)

### 2. Knowledge Base Layer
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: ChromaDB with patient_id metadata
- **Chunking**: Semantic chunking (512 tokens)

### 3. Retrieval Layer
- **Query Encoding**: Same embedding model
- **Filtering**: Strict patient_id filter (metadata)
- **Re-ranking**: Similarity threshold + Top-K

### 4. Generation Layer
- **LLM**: Google Gemini 2.0 Flash (free API)
- **Prompt Engineering**: System + context + query
- **Post-processing**: Citation extraction

### 5. MLOps Layer
- **Versioning**: Models, data, configurations
- **Monitoring**: Retrieval metrics, answer quality
- **Evaluation**: Automated testing pipeline

## Data Flow
1. Patient uploads clinical notes (in real system)
2. Notes de-identified and chunked
3. Chunks embedded and stored with patient_id tag
4. User selects patient and asks question
5. Query embedded and retrieves patient-specific chunks
6. LLM synthesizes answer from chunks
7. Answer returned with citations

## Privacy Guarantees
- Patient data tagged at ingestion
- Vector store queries filtered by patient_id
- Privacy audit tests for cross-patient leakage
- De-identification validation at every step
