import os
import pandas as pd

class DataIngestion:

    def __init__(self,data_path="artifacts"):
        self.movies_path=os.path.join(data_path,"tmdb_5000_movies_raw.csv")
        self.credits_path=os.path.join(data_path,"tmdb_5000_credits_raw.csv")

    def load_and_merge(self):
        movies=pd.read_csv(self.movies_path)
        credits=pd.read_csv(self.credits_path)

        credits.rename(columns={'movie_id':'id'},inplace=True)

        df=movies.merge(credits,on='id')
        df.rename(columns={'title_x':'title'},inplace=True)
        df.drop('title_y',axis=1,inplace=True)
        return df