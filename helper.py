import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

Books=pd.read_csv("Books.csv")
Users=pd.read_csv("Users.csv") 
Ratings=pd.read_csv("Ratings.csv")

def popular_books():
    # count ratings
    rating_with_name = pd.merge(Books,Ratings,on="ISBN")
    num_rating_df=rating_with_name.groupby("Book-Title").count()["Book-Rating"].reset_index()
    num_rating_df.rename(columns ={"Book-Rating":"num_ratings"},inplace=True)
    
    # average rating
    avg_rating_df =rating_with_name.groupby("Book-Title").agg({"Book-Rating":"mean"}).reset_index()
    avg_rating_df.rename(columns={"Book-Rating":"avg_rating"},inplace=True)
    
    # filter top books
    popular_df = num_rating_df.merge(avg_rating_df,on="Book-Title")
    popular_df= popular_df[popular_df["num_ratings"]>= 250].sort_values("avg_rating",ascending=False).head(50)
    popular_df=popular_df.merge(Books,on="Book-Title").drop_duplicates("Book-Title")[["Book-Title","Book-Author","Image-URL-M","num_ratings","avg_rating"]]

    return popular_df


# collabarative recomendation system

rating_with_name = pd.merge(Books,Ratings,on="ISBN")
x = rating_with_name.groupby("User-ID")["Book-Title"].count() > 200
padhe_likhe_user = x[x].index

filtered_rating = rating_with_name[rating_with_name["User-ID"].isin(padhe_likhe_user)]
y = filtered_rating.groupby("Book-Title")["Book-Rating"].count()>=50
famous_books = y[y].index

final_rating = filtered_rating[filtered_rating["Book-Title"].isin(famous_books)]
pt = final_rating.pivot_table(index="Book-Title",columns="User-ID",values="Book-Rating")
pt.fillna(0,inplace=True)


# similarity_score = cosine_similarity(pt)
    
def book_recomend(book_name):
     # index fetch 
     similarity_score = cosine_similarity(pt)

     index = np.where(pt.index == book_name)[0][0]
     similar_items = sorted(list(enumerate(similarity_score[index])),key = lambda x:x[1],reverse=True)[1:6]

     recommendations = []

     for i in similar_items:
        recommendations.append(pt.index[i[0]])
        
     return recommendations