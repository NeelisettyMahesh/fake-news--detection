import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load datasets
movie_data = pd.read_csv("movies.csv")
rating_data = pd.read_csv("ratings.csv")

# Configure Streamlit
st.set_page_config(page_title="🎥 Movie Match Maker", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎬 Smart Movie Match Maker</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Prepare user-movie matrix
ratings_matrix = rating_data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
id_to_title = dict(zip(movie_data['movieId'], movie_data['title']))
title_to_id = dict(zip(movie_data['title'], movie_data['movieId']))

# Compute cosine similarity
sparse_movies = csr_matrix(ratings_matrix.T.values)
similarity_matrix = cosine_similarity(sparse_movies)

# Map index and ids
movie_ids = list(ratings_matrix.columns)
index_lookup = {mid: idx for idx, mid in enumerate(movie_ids)}
reverse_lookup = {idx: mid for idx, mid in enumerate(movie_ids)}

# UI input
st.markdown("### 🎯 Select a movie you like:")
user_selected_movie = st.selectbox("", sorted(movie_data['title'].unique()))

# Recommendation logic
def suggest_movies(movie_title, top_n=5):
    movie_id = title_to_id.get(movie_title)
    if movie_id not in index_lookup:
        return []
    idx = index_lookup[movie_id]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_suggestions = scores[1:top_n+1]
    result = []
    for i, score in top_suggestions:
        movie = id_to_title.get(reverse_lookup[i], "Unknown")
        result.append((movie, round(score, 2)))
    return result

# Output display
if user_selected_movie:
    st.markdown("### 🔍 Suggested Movies Just for You")
    st.markdown("Here are some movies similar to your choice, based on user ratings:")
    results = suggest_movies(user_selected_movie)

    for title, score in results:
        st.markdown(f"""
            <div style='padding: 15px; background-color: #2c2f33; 
                        border-radius: 10px; margin-bottom: 12px; color: #f1f1f1;
                        border: 1px solid #444;'>
                <strong style='font-size: 16px;'>🎞️ {title}</strong><br>
                <span style='font-size: 14px; color: #bbb;'>Similarity Score: {score}</span>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><hr style='margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
