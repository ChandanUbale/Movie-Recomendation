# -*- coding: utf-8 -*-
"""Movie-Recomendation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BNfR6zMR53E_MneVErtaXQPTWT8TXTqi
"""

import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.shape

df.columns

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre']+' '+df_features['Movie_Keywords']+' '+df_features['Movie_Tagline']+' '+df_features['Movie_Cast']+' '+df_features['Movie_Director']

x

x.shape

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

from sklearn.metrics.pairwise import cosine_similarity

Similarity_Score = cosine_similarity(x)

Similarity_Score

Similarity_Score.shape

Favourite_Movie_Name = input('Enter Your Favourite Movie Name : ')

All_Movies_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recomendation = difflib.get_close_matches(Favourite_Movie_Name,All_Movies_Title_List)

print(Movie_Recomendation)

Close_Match = Movie_Recomendation[0]

print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

# Getting a lis of similar movies
Recomendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print(Recomendation_Score)

len(Recomendation_Score)

#sorting all movies based on their similarity score
Sorted_Similar_Movies = sorted(Recomendation_Score,key = lambda x:x[1],reverse =True)
print(Sorted_Similar_Movies)

#printing similar movies based on their index
print('Top 30 movies for you :\n')
i=1
for movie in Sorted_Similar_Movies:
  index =movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if(i<31):
    print(i,' ',title_from_index)
    i+=1

import difflib

# Assuming you have already loaded your DataFrame 'df' and calculated 'Similarity_Score'

# Step 1: Input your favorite movie
Movie_Name = input('Enter Your Favorite Movie Name: ')

# Step 2: Find a close match using difflib
list_of_all_titles = df['Movie_Title'].tolist()
Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)
Close_Match = Find_Close_Match[0]

# Step 3: Get the index of the close-matched movie
Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]

# Step 4: Create a list of movie recommendations with their similarity scores
Recomendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))

# Step 5: Sort the similar movies by their scores in descending order
Sorted_Similar_Movies = sorted(Recomendation_Score, key=lambda x: x[1], reverse=True)

# Step 6: Print the top 10 recommended movies
print('Top 10 movies:\n')
i = 1
for movie in Sorted_Similar_Movies:
    index = movie[0]
    title_from_index = df[df.index == index]['Movie_Title'].values[0]
    if i < 11:
        print(i, ' ', title_from_index)
        i += 1