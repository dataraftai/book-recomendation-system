import streamlit as st
import pandas as pd

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


