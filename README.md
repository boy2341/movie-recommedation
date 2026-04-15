# Movie Recommendation System

This project is a content-based recommendation engine developed using Python and Streamlit. It leverages the IMDB Top 1000 dataset to suggest films based on metadata similarities such as genre, director, and lead actors.

## Technical Architecture

The application implements a natural language processing (NLP) pipeline to determine the mathematical proximity between different titles.

### 1. Data Processing
The system focuses on six core features to determine similarity:
* Genre
* Director
* Top 4 Lead Actors (Star1 through Star4)

All missing values are handled during the preprocessing stage, and these features are concatenated into a single "metadata string" for each movie.

### 2. Vectorization
The combined metadata is converted into a numerical format using **CountVectorizer**. This process:
* Removes common English stop words.
* Creates a sparse matrix representing the frequency of relevant terms across the dataset.

### 3. Similarity Metric
The core recommendation logic is powered by **Cosine Similarity**. By calculating the cosine of the angle between two vectors in a multi-dimensional space, the system produces a score ranging from 0 to 1. A score of 1 indicates identical metadata, while 0 indicates no shared characteristics.

## UI and Experience

The interface is built with Streamlit and features a custom visual layer:
* **Background Integration**: Uses Base64 encoding to inject a local image directly into the application's CSS.
* **Interactive Querying**: Real-time text input allowing users to search for any title in the IMDB Top 1000 list.
* **Dynamic Feedback**: Displays the top five recommendations along with their calculated similarity scores.

## Setup Instructions

### Prerequisites
Ensure the following Python libraries are installed:
* streamlit
* pandas
* numpy
* scikit-learn

### Local Execution
1.  Verify that `imdb_top_1000.csv` and your background image `img.jpg` are in the project root folder.
2.  Launch the application using:
    ```bash
    streamlit run app.py
    ```

## Project Logic Flow
1.  **Input**: User enters a movie name.
2.  **Processing**: The system identifies the index of the movie and retrieves its pre-computed similarity vector.
3.  **Ranking**: The system sorts all other movies based on their similarity scores in descending order.
4.  **Output**: The top five most similar titles are rendered to the screen.
