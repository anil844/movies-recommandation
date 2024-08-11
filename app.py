import pickle
import streamlit as st

# Load the pre-trained models and data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit interface
st.header('Movie Recommender System')

# Dropdown for selecting a movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Function to recommend movies based on similarity
def recommend_movies(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    # Get the similarity scores for the selected movie
    similar_movies = list(enumerate(similarity[movie_index]))
    # Sort movies based on similarity score
    sorted_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    # Get the top 5 recommended movies (excluding the selected movie)
    recommended_movies = [movies['title'].iloc[i[0]] for i in sorted_movies[1:6]]
    return recommended_movies

# Display recommended movies
if selected_movie:
    recommendations = recommend_movies(selected_movie)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
