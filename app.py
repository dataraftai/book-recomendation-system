import streamlit as st
import pandas as pd
# Import data and functions from your helper file (must be in the same directory)
from helper import popular_books, book_recomend, pt, Books 

popular_df = popular_books()

# --- 1. Streamlit UI Configuration ---
st.set_page_config(
    layout="wide", 
    page_title="Book Recommender", 
    page_icon="📚"
)

st.title("📚 Book Recommendation Engine")
st.markdown("---")

# --- 2. Recommendation System Section (Using Native Containers) ---

# Use a native container to visually group the recommendation section
with st.container(border=True): 
    st.header("🔎 Find Similar Reads")
    st.markdown("Select a book you loved, and we'll suggest five similar titles using collaborative filtering.")
    
    # Check if the collaborative filtering pivot table is ready
    if not pt.empty:
        option = st.selectbox(
            "**Select a book you love:**", 
            pt.index, 
            index=None,
            placeholder="Choose a book to get started..."
        )

        if st.button("Get Recommendations", type="primary"):
            if option:
                st.subheader(f"Top 5 Recommendations for: *{option}*")
                
                # Get recommendations
                recs = book_recomend(option)
                recommendation_details = Books[Books['Book-Title'].isin(recs)].drop_duplicates('Book-Title')
                
                # Create 5 columns for horizontal display
                cols = st.columns(5)
                
                for i, rec_title in enumerate(recs):
                    rec_info = recommendation_details[recommendation_details['Book-Title'] == rec_title]
                    
                    if not rec_info.empty:
                        rec_info = rec_info.iloc[0]
                        image_url = rec_info['Image-URL-M']
                        author = rec_info['Book-Author']
                    else:
                        image_url = "https://placehold.co/100x150/cccccc/333333?text=No+Image"
                        author = "Unknown Author"

                    with cols[i]:
                        # Use a small container for each recommendation card
                        with st.container(border=True):
                            st.image(image_url, caption="", width=100)
                            st.caption(f"**{rec_title}**")
                            st.caption(f"*{author}*")
            else:
                 st.warning("Please select a book to receive recommendations.")
    else:
        st.error("Recommendation model data is not available. Please ensure your CSV files are correctly loaded and the filtering logic in `helper.py` works.")

st.markdown("---")

# --- 3. Most Popular Books Section (Using Native Metrics) ---

st.header("🔥 Top 50 Most Popular Books")
st.info("These are the most highly-rated books based on a minimum of 250 reviews.")

# Ensure popular_df has content before trying to iterate
if not popular_df.empty:
    
    # Display in a 3-column grid
    for i in range(0, len(popular_df), 3):
        cols = st.columns(3)

        for idx, col in enumerate(cols):
            if i + idx < len(popular_df):
                row = popular_df.iloc[i + idx]
                rank = i + idx + 1

                with col:
                    # Use a container for a clean card look for each book
                    with st.container(border=True): 
                        
                        # Use small columns to align image and stats nicely
                        img_col, stats_col = st.columns([1, 2])
                        
                        with img_col:
                            st.image(row['Image-URL-M'], width=90)
                        
                        with stats_col:
                            # Use st.metric for a "cool" card look for the numbers
                            st.metric(label="Rank", value=f"#{rank}")
                            st.metric(label="Rating", value=f"⭐ {round(row['avg_rating'], 2)}", delta_color="off")
                            st.caption(f"({row['num_ratings']:,} ratings)")
                        
                        st.divider()
                        # Use subheader for prominent book title
                        st.subheader(row['Book-Title'])
                        st.markdown(f"*{row['Book-Author']}*")
else:
    st.error("No popular books data available. Check data loading in `helper.py`.")