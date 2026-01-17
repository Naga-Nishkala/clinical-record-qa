# 01 - Data Generation

## Purpose
Generate synthetic clinical notes for 10 patients to simulate realistic EHR data.

## Notebooks
- `synthetic_clinical_notes_generator.ipynb` - Main data generation notebook

## Outputs
- `raw_clinical_notes/` - Individual patient folders with clinical notes
- `patient_metadata.json` - Patient demographics and visit information
- `generation_summary.csv` - Statistical summary of generated data
- `mlops_generation_log.json` - Reproducibility tracking

## Key Features
- 5 medical conditions (Diabetes, Hypertension, Asthma, CKD, Hyperlipidemia)
- 3-5 visits per patient over 2 years
- Realistic medications, lab values, and clinical assessments
- Reproducible generation (seed=42)
