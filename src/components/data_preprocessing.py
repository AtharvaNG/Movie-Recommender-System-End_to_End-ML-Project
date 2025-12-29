import pandas as pd
import ast

def select_relevant_columns(df):
    # keep only relevant columns in the data

    df=df[['id','title','overview','genres','keywords','cast','crew']].copy()  #copy() to modify the real df and not just to return a copy
    df.dropna(inplace=True)  # there we 3 rows with overview as null , so we decided to drop those rows
    return df


def convert(obj):  #to convert genres and keywords
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


def convert_cast(obj):
    L=[]
    count=0
    for i in ast.literal_eval(obj):
        if count<3:
            L.append(i['name'])
            count+=1
        else:
            break
    return L

def convert_crew(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
            break
    
    return L



def apply_basic_cleaning(df):
    df['genres']=df['genres'].apply(convert)
    df['keywords']=df['keywords'].apply(convert)
    df['cast']=df['cast'].apply(convert_cast)
    df['crew']=df['crew'].apply(convert_crew)
    df['overview']=df['overview'].apply(lambda x:x.split())  #converting string to list of words


    #removing spaces between words  eg. "Sam Worthington" to "SamWorthington"
    df['genres']=df['genres'].apply(lambda x: [i.replace(" ","") for i in x])
    df['keywords']=df['keywords'].apply(lambda x: [i.replace(" ","") for i in x])
    df['cast']=df['cast'].apply(lambda x: [i.replace(" ","") for i in x])
    df['crew']=df['crew'].apply(lambda x: [i.replace(" ","") for i in x])

    #creating tags
    df['tags']=df['overview']+df['genres']+df['keywords']+df['cast']+df['crew']

    #converting tags to single sentence and lower case
    df['tags']=df['tags'].apply(lambda x:" ".join(x))
    df['tags']=df['tags'].apply(lambda x:x.lower())

    #creating final df
    final_df=df[['id','title','tags']]
    return final_df