from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import select_relevant_columns,apply_basic_cleaning
from src.components.feature_engineering import generate_similarity,generate_vectors

import pickle,os

def train_and_save():
    #1. Load + merge
    df=DataIngestion().load_and_merge()
    
    #2. Preprocessing
    df=select_relevant_columns(df)
    final_df=apply_basic_cleaning(df)

    #3. Vectorization + similarity
    vectors=generate_vectors(final_df)
    similarity=generate_similarity(vectors)

    #4. Save artifacts

    os.makedirs("artifacts",exist_ok=True)

    pickle.dump(final_df,open("artifacts/movie_df.pkl","wb"))
    pickle.dump(similarity,open("artifacts/similarity.pkl","wb"))


if __name__=="__main__":
    train_and_save()
