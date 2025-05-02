import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎬 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)
st.markdown("### Select a movie you like and get 5 recommendations!", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Choose a movie:',
    movies['title'].values,
    index=0,
    help="Pick a movie from the dropdown to get recommendations"
)

if st.button('🎥 Recommend Movies'):
    recommendations = recommend(selected_movie_name)

    st.markdown("---")
    st.subheader("✨ Recommended Movies:")
    col1, col2 = st.columns(2)

    for idx, movie in enumerate(recommendations):
        if idx % 2 == 0:
            with col1:
                st.success(f"📌 {movie}")
        else:
            with col2:
                st.success(f"📌 {movie}")
else:
    st.info("👆 Click the **Recommend Movies** button to see suggestions.")
