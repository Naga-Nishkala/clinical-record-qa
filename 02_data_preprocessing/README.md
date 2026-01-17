# 02 - Data Preprocessing

## Purpose
De-identify clinical notes and validate data quality before downstream processing.

## Notebooks
- `deidentification_pipeline.ipynb` - Remove PHI (names, dates, etc.)
- `quality_validation.ipynb` - Validate de-identification completeness

## Outputs
- `deidentified_notes/` - Sanitized clinical notes
- `deidentification_logs/` - What was redacted and confidence scores

## Key Features
- Presidio-based PHI detection
- Pattern-based entity removal
- Validation metrics (recall, precision)
- Compliance logging for audit trails
