# Development Guide

## Getting Started

### Prerequisites
- Google Account (for Colab and Drive)
- Google Gemini API key (free tier)
- Basic Python knowledge

### Setup
1. Run `00_project_setup.ipynb` to create folder structure
2. Run notebooks sequentially (01 → 02 → ... → 08)
3. Each notebook saves outputs to Google Drive
4. Outputs from one notebook feed into the next

## Development Workflow

### Phase 1: Data Preparation (Notebooks 01-02)
1. Generate synthetic clinical notes
2. De-identify and validate data
3. Verify data quality

### Phase 2: Knowledge Base (Notebooks 03-04)
1. Generate embeddings
2. Build vector store
3. Test retrieval with patient filtering

### Phase 3: Q&A System (Notebooks 05-07)
1. Integrate LLM
2. Build RAG pipeline
3. Create interactive demo

### Phase 4: Evaluation (Notebook 08)
1. End-to-end testing
2. Privacy audit
3. Performance metrics

## Best Practices

### Code Organization
- Keep notebooks focused on single tasks
- Extract reusable code to `utils/`
- Use configuration files for parameters

### Data Management
- Version all datasets (v1.0, v1.1, etc.)
- Log data transformations
- Validate data at each step

### MLOps
- Track all experiments
- Version models and embeddings
- Monitor system performance

## Troubleshooting

### Common Issues
- **Out of memory**: Reduce batch size in embeddings
- **Slow retrieval**: Reduce top_k or add similarity threshold
- **Poor answers**: Adjust prompt templates or increase context

## Migration to GitHub
1. Clean notebooks (remove hardcoded paths)
2. Add requirements.txt
3. Update README with installation instructions
4. Test end-to-end on fresh environment
