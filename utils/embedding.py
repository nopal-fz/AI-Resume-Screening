from sentence_transformers import SentenceTransformer

# load model untuk embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# fungsi untuk mendapatkan embeddings dari teks
def get_embeddings(text):
    return model.encode(text)