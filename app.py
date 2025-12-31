import streamlit as st
from src.components.recommender import recommend,movies

st.title("Movie Recommender System")

movie_list=movies['title'].values

selected_movie=st.selectbox("Select a movies:",movie_list)

if st.button("Recommend"):
    names,posters,error=recommend(selected_movie)
    
    
    if error:
        st.error(error)
    else:
        cols=st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])


