import pickle
import requests
import time
from dotenv import load_dotenv
import os


#Load artifacts
movies=pickle.load(open("artifacts/movie_df.pkl","rb"))
similarity=pickle.load(open("artifacts/similarity.pkl","rb"))

#this fetch_poster code is not working because we are 5 api request at one recommendation so it is geting crashed , it is problem of the api/tmdb not the code.  
# def fetch_poster(movie_id):
#     
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
#     data = requests.get(url).json()
    
#     poster_path = data.get("poster_path")
    
#     return f"https://image.tmdb.org/t/p/w500{poster_path}"

load_dotenv()  #loads variables form .env
API_KEY=os.getenv("TMDB_API_KEY")
session = requests.Session()
def fetch_poster(movie_id, retries=3):
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    
    for _ in range(retries):
        try:
            response = session.get(url, timeout=5)  # reuse session
            if response.status_code == 200:
                data = response.json()
                poster_path = data.get('poster_path')
                return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
        except requests.exceptions.RequestException:
            continue

    return None

def recommend(movie_name):
    
    if movie_name not in movies['title'].values:
        return [],[],"Movie not found"

    movie_index=movies[movies['title']==movie_name].index[0]

    sim_arr=similarity[movie_index] #similarity metrics (array) of the movie with othe movies

    movies_list=sorted(list(enumerate(sim_arr)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_titles=[]
    recommended_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_titles,recommended_posters,None


