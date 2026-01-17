# 04 - Retrieval System

## Purpose
Build and evaluate patient-specific retrieval with strict data isolation.

## Notebooks
- `patient_specific_retriever.ipynb` - Implement filtered retrieval
- `retrieval_evaluation.ipynb` - Measure Hit@K, MRR, patient leakage

## Outputs
- `retrieval_metrics/` - Performance metrics per patient

## Key Features
- Patient_id filtering (zero cross-contamination)
- Top-K retrieval with re-ranking
- Retrieval quality metrics
- Patient isolation testing
