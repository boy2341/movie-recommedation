import streamlit as st
import pandas as pd
import numpy as np  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# Loading dataset (SOURCE - Kagle)
df = pd.read_csv("imdb_top_1000.csv") # ----> Dataset with 1000 toprated movies with ratings, cast, grossing etc..



# Select useful columns and fill blanks
features = ['Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4'] # -----> Judgment Critereon for similarity

for col in features:
    df[col] = df[col].fillna('') # ----> Traversing each column to clean the dataset



# Combine selected features into one string for easy vectorization
def combine_features(row):
    return ' '.join([row['Genre'], row['Director'], row['Star1'], row['Star2'], row['Star3'], row['Star4']])

df['combined_features'] = df.apply(combine_features, axis=1) #-----> Make an extra row consisting of a string with all the features selected


# Vectorize text
cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(df['combined_features'])


# Compute similarity
similarity = cosine_similarity(count_matrix)


# Recommendation function
def recommend(movie_name, n=5):
    movie_name = movie_name.lower()
    if movie_name not in df['Series_Title'].str.lower().values:
        st.write("❌❌❌ Movie not found. Please check spelling or The Movie is Not in the Database ❌❌❌")
        return
    
    # find movie index
    index = df[df['Series_Title'].str.lower() == movie_name].index[0]
    
    # similarity scores for that movie
    scores = list(enumerate(similarity[index])) # ----> Makes a list with similarity scores assigned to each index value
    
    # sort by similarity score (excluding itself)
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1] #-----> We ignore the 0 index as it is the movie itself


    
    st.write(f"\n Top {n} movies similar to '{df.iloc[index]['Series_Title']}' are:\n")


    for i, score in sorted_scores:
        st.write(f"👉 {df.iloc[i]['Series_Title']}  |  Score: {round(score, 2)}")
#entering movie name to get recommendations
st.text_input("Enter the movie name" , key ="movie_entry")
movie_input=st.session_state.movie_entry
st.write("You entered: ", movie_input)
#recommendation output
st.write(recommend(movie_input))    
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Replace 'your_image.jpg' with your actual file path
add_bg_from_local('img.jpg')
