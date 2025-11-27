import streamlit as st
import pandas as pd
from helper import popular_books, book_recomend, pt
import helper


popular_df = popular_books()

st.title("Most Popular Books")

# Display in grid (3 per row)
for i in range(0,len(popular_df),3):
    cols = st.columns(3)

    for idx, col in enumerate(cols):
        if i + idx < len(popular_df):
            row = popular_df.iloc[i + idx]

            
            with col:
                st.image(row["Image-URL-M"],width=150)
                st.markdown(f"**{row['Book-Title']}**")
                st.markdown(f"*by {row['Book-Author']}*")
                st.markdown(f"⭐ {round(row['avg_rating'],1)} - {row['num_ratings']} ratings")
                st.write("---")


st.title("Book Recommendation System")

option = st.selectbox("Select a book", pt.index)

if st.button("Recommend"):
    recs = book_recomend(option)
    for book in recs:
        st.write(book)


st.set_page_config(layout="wide")