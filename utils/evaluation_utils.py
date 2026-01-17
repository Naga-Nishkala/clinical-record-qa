"""
Evaluation metrics and utilities.

Functions:
- calculate_retrieval_metrics(): Hit@K, MRR
- calculate_answer_metrics(): Faithfulness, relevance
- check_patient_leakage(): Verify data isolation
"""

def calculate_retrieval_metrics(retrieved, ground_truth):
    """Calculate retrieval performance metrics"""
    # TODO: Implement in notebook 08
    pass

def calculate_answer_metrics(answer, ground_truth, retrieved_chunks):
    """Calculate answer quality metrics"""
    # TODO: Implement in notebook 08
    pass

def check_patient_leakage(retrieval_results, patient_id):
    """Verify no data leakage across patients"""
    # TODO: Implement in notebook 08
    pass
