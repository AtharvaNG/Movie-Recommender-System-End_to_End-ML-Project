# Movie Recommender System

A content-based movie recommendation system that suggests similar movies using NLP techniques and cosine similarity, deployed as a web application.

---

## Overview
Choosing a movie to watch can be overwhelming due to the large number of available options.  
This project solves that problem by recommending movies similar to a selected title based on textual metadata such as overview, genres, keywords, cast, and director.

---

## Key Features
- Content-based movie recommendations using NLP (Bag of Words + cosine similarity)
- Modular machine learning pipeline for data ingestion, preprocessing, feature engineering, and inference
- Runtime similarity computation with caching to handle cloud deployment constraints
- TMDB API integration for dynamic movie poster fetching with retry and rate-limit handling
- Deployed web interface using Streamlit on Render

---

## Tech Stack
- **Language:** Python  
- **Framework / Libraries:** Pandas, NumPy, Scikit-learn, Streamlit, Requests  
- **Tools:** Git, GitHub, Render, TMDB API  

---

## Project Structure
```text
Movie-Recommender-System/
│── artifacts/
│   └── movie_df.pkl
│── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_preprocessing.py
│   │   ├── feature_engineering.py
│   │   └── recommender.py
│   └── pipeline/
│       └── train_pipeline.py
│── app.py
│── requirements.txt
│── README.md
The project is organized into clear components to separate data processing, model logic, and application code.

```

---

## Setup & Run
git clone https://github.com/AtharvaNG/Movie-Recommender-System-End_to_End-ML-Project.git

cd Movie-Recommender-System-End_to_End-ML-Project

pip install -r requirements.txt

streamlit run app.py

Note: A TMDB API key is required to fetch movie posters.

Set it as an environment variable:
TMDB_API_KEY=your_api_key

---

## Output
A web interface where users select a movie from a dropdown

Displays the top recommended similar movies along with their posters

Recommendations are generated using cosine similarity on textual movie features

---

## Author
Atharva Nitin Gholap

GitHub: https://github.com/AtharvaNG

LinkedIn: https://www.linkedin.com/in/atharva-gholap-67739828b/
