## 📚 Collaborative Filtering Book Recommendation Engine

### ✨ Project Overview

This is a full-stack data science application designed to provide two key features: a list of the top 50 most popular books and a personalized recommendation engine based on user behavior.

The core technology uses a Collaborative Filtering (CF) model to identify hidden relationships between books, ensuring high-quality, relevant suggestions for the user. The application is built entirely in Python, making it robust, fast, and easy to deploy.

### 🚀 Features

Top 50 Popular Books: Displays the 50 highest-rated books, filtered to ensure they have a minimum number of ratings (250+).

Personalized Recommendations: Given any book in the model's index, the system suggests five highly similar titles.

Modern UI: A clean, responsive user interface built using Streamlit that utilizes native components (st.container, st.columns, st.metric) for a professional, card-based look.

### 💻 Tech Stack

Component

Technology

Role

Data Science

Python (Pandas, NumPy)

Data cleaning, filtering, and transformation.

Machine Learning

Scikit-learn (cosine_similarity)

Model inference and calculating item-to-item similarity.

Application UI

Streamlit

Rapid development of the interactive web application.

Version Control

Git / GitHub

Code management and collaboration.

### ⚙️ Methodology (How the Recommender Works)

The recommendation engine is built using Item-to-Item Collaborative Filtering.

Data Filtering: To ensure model accuracy and manage data sparsity, the raw data is filtered:

Users: Only users who have rated more than 200 books are included.

Books: Only books that have received at least 50 ratings are included.

Pivot Table Creation: The filtered data is transformed into a User-Item Pivot Table (pt) where book titles form the index, User IDs form the columns, and the rating is the value.

Similarity Calculation: The core of the model is calculated by running the cosine_similarity function on the pivot table. This generates a matrix where each row represents a book, and the values indicate how similar that book is to every other book.

Inference: When a user selects a book, the model looks up that book's index in the similarity matrix, sorts the scores, and returns the top 5 most similar books.

### 🛠️ Setup 

Clone the Repository (or create the files):

git clone <your-repo-link>
cd book-recommendation-engine


📂 Project Structure

.
├── Books.csv
├── Users.csv
├── Ratings.csv
├── app.py           # Main Streamlit UI and frontend logic
├── helper.py        # Core data loading, filtering, and recommendation functions
└── README.md        # This file


### 👨‍💻 Contribution and Contact

Feel free to fork this repository, suggest improvements, or submit pull requests.

Author: [Your Name]

GitHub: [Your GitHub Profile Link]