## 📚 Collaborative Filtering Book Recommendation Engine

### ✨ Project Overview

This is a full-stack data science application designed to provide two key features: a list of the top 50 most popular books and a personalized recommendation engine based on user behavior.

The core technology uses a Collaborative Filtering (CF) model to identify hidden relationships between books, ensuring high-quality, relevant suggestions for the user. The application is built entirely in Python, making it robust, fast, and easy to deploy.

### 🖼️ App Screenshots / Demo

<img src="(images/Screenshot (20).png" width="850">

1. The Recommendation Finder

(This screenshot will show the section where the user selects a book and gets the 5 suggestions in the nice card format.)
<img src="(images/Screenshot (23).png" width="850">

2. The Popular Books Grid

(This screenshot will show the scrollable grid of the Top 50 books with their ratings and authors.)

<img src="(images/Screenshot (22).png" width="850">


### 🚀 Key Features

Top 50 Popular Books: Displays the 50 highest-rated books, filtered to ensure they have a minimum number of ratings (250+).

Personalized Recommendations: Given any book in the model's index, the system suggests five highly similar titles.

Modern UI: A clean, responsive user interface built using Streamlit that utilizes native components (st.container, st.columns, st.metric) for a professional, card-based look.

### 💻 Tech Stack

Role : Data Science

- Technology : Python (Pandas, NumPy)

  Data cleaning, filtering, and transformation.

- Scikit-learn (cosine_similarity) : Model inference and calculating item-to-item similarity.

- Streamlit : Rapid development of the interactive web application.

- Version Control : Git / GitHub


### 📂 Project Structure

``` text
.
├── app.py           # The Streamlit web interface (what the user sees)
├── helper.py        # All the data loading, cleaning, and model logic
├── requirements.txt # List of all required Python libraries (e.g., streamlit, pandas)
├── .gitignore       # Specifies files/folders Git should ignore (e.g., __pycache__)
└── README.md        # This file

```
### ⚙️ Methodology (How the Recommender Works)

The recommendation engine is built using Item-to-Item Collaborative Filtering.

Data Filtering: To ensure model accuracy and manage data sparsity, the raw data is filtered:

Users: Only users who have rated more than 200 books are included.

Books: Only books that have received at least 50 ratings are included.

Pivot Table Creation: The filtered data is transformed into a User-Item Pivot Table (pt) where book titles form the index, User IDs form the columns, and the rating is the value.

Similarity Calculation: The core of the model is calculated by running the cosine_similarity function on the pivot table. This generates a matrix where each row represents a book, and the values indicate how similar that book is to every other book.

Inference: When a user selects a book, the model looks up that book's index in the similarity matrix, sorts the scores, and returns the top 5 most similar books.
