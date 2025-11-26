import streamlit as st
import pandas as pd
import helper


st.title("Most Popular Books")

popular_df = helper.popular_books()

# Display in grid (3 per row)
for i in range(0,len(popular_df),3):
    cols = st.columns(3)

    for idx, col in enumerate(cols):
        if i + idx < len(popular_df):
            row = popular_df.iloc[i + idx]

            
            with col:
                st.image(row["Image-URL-M"],width=150)
                st.markdown(f"**{row["Book-Title"]}**")
                st.markdown(f"*by {row["Book-Author"]}*")
                st.markdown(f"⭐ {round(row["avg_rating"],2)} - {row["num_ratings"]} ratings")
                st.write("---")