🧠 Model Description
This project is a Content-Based Movie Recommendation System built using the TMDB 5000 Movies Dataset. The system recommends movies similar to a selected title based on metadata such as genres, cast, crew, keywords, and movie overview.

🔄 Data Preprocessing
Merged tmdb_5000_movies.csv and tmdb_5000_credits.csv on the title column.

Selected relevant columns: movie_id, title, overview, genres, keywords, cast, crew.

Removed missing values and duplicates.

Extracted:

Top 3 cast members.

Director from the crew.

Names from genres and keywords.

Removed spaces in multi-word tokens and converted all text to lowercase.

🛠 Feature Engineering
Combined overview, keywords, cast, and crew into a new column tags.

Applied stemming using NLTK's PorterStemmer to normalize text.

🔍 Vectorization & Similarity
Used CountVectorizer with max_features=5000 and stop_words='english' to convert tags into a numerical vector (Bag-of-Words model).

Computed cosine similarity between movie vectors to measure similarity.

🎯 Recommendation Logic
For a given movie, the system finds its vector and computes similarity scores with all other movies.

Returns the top 5 most similar movies (excluding the input movie).
