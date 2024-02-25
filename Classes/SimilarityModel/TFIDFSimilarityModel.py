from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# TODO: change this method to calss in the future.
def average_pairwise_similarity(articles):
    # Vectorize the articles using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(articles)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    np.fill_diagonal(similarity_matrix, 0)

    n_articles = len(articles)
    avg_similarity = np.sum(similarity_matrix) / (n_articles * (n_articles - 1))

    return avg_similarity