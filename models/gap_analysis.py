from sklearn.metrics.pairwise import cosine_similarity
from utils.embedding import get_embeddings

# menghitung similarity antara CV dan JD
def analyze_gap(cv_embeddings, jd_embeddings):
    similarity = cosine_similarity([cv_embeddings], [jd_embeddings])
    return similarity[0][0]

# mencari job yang paling sesuai dengan CV
def adaptive_matching(cv_text, available_jobs):
    best_match = None
    highest_score = 0
    for job in available_jobs:
        job_embeddings = get_embeddings(job['description'])
        cv_embeddings = get_embeddings(cv_text)
        score = analyze_gap(cv_embeddings, job_embeddings)
        if score > highest_score:
            highest_score = score
            best_match = job
    return best_match
