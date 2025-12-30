#Vectorization
#vectors of each movies will basically contain the frequency of most repeating 5,000 words from all the tags(technique -> bag of words)


from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def generate_vectors(df):
    cv=CountVectorizer(max_features=5000, stop_words='english')
    vectors=cv.fit_transform(df['tags']).toarray()
    return vectors

def generate_similarity(vectors):
    similarity=cosine_similarity(vectors)
    return similarity


