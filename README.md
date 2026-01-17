# Clinical Notes Q&A System
## Personalized Patient Q&A using GenAI + MLOps

### 🎯 Project Overview
This project builds a production-level Q&A system that allows patients to interact with their clinical notes using natural language queries. The system ensures:
- **Patient data isolation**: Each patient only accesses their own records
- **Intelligent synthesis**: Not just chunk retrieval, but reasoned answers
- **Citation transparency**: Every answer cites source clinical notes
- **Privacy-first**: De-identification pipeline before processing

### 🏗️ Architecture
```
Synthetic Data → De-identification → Embedding Generation → Vector Store
                                                                 ↓
Patient Query → Filtered Retrieval → LLM Reasoning → Cited Answer
```

### 📂 Project Structure
- `01_data_generation/` - Synthetic clinical notes generation
- `02_data_preprocessing/` - De-identification and data cleaning
- `03_knowledge_base/` - Embedding generation and vector store setup
- `04_retrieval_system/` - Patient-specific retrieval logic
- `05_qa_generation/` - RAG pipeline with LLM integration
- `06_mlops_artifacts/` - Model versioning, experiment tracking, monitoring
- `07_inference_demo/` - Interactive patient Q&A chatbot
- `08_evaluation/` - End-to-end testing and evaluation
- `config/` - Configuration files for models, prompts, patients
- `utils/` - Reusable Python utilities
- `docs/` - Documentation and guides

### 🚀 Technology Stack (100% Free & Local)
- **LLM**: TinyLlama 1.1B Chat (Local inference, no API)
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: ChromaDB (local)
- **De-identification**: Regex-based PHI removal
- **Development**: Google Colab + Google Drive
- **Interface**: Gradio (web UI with shareable links)

### 📊 MLOps Features
- Data versioning and lineage tracking
- Experiment logging (hyperparameters, metrics)
- Model registry with versioning
- Retrieval and generation metrics
- Privacy compliance auditing

### 🔒 Privacy & Safety
- Synthetic data only (no real patient information)
- De-identification validation at every step
- Patient isolation guarantees (zero cross-contamination)
- Citation transparency for all answers

### 📝 Getting Started
1. Run `00_project_setup.ipynb` to create folder structure
2. Run `01_synthetic_clinical_notes_generator.ipynb` to generate data
3. Follow notebooks sequentially (02 → 03 → ... → 08)
4. Use `07_inference_demo.ipynb` for interactive Q&A

### 📅 Project Timeline
- **Created**: January 2026
- **Data Version**: v1.0
- **Status**: Development Phase (Google Drive + Colab) with GitHub migration

### 👤 Author
Clinical Notes Q&A System Project

---
*This project demonstrates production-level MLOps practices for healthcare GenAI applications.*
