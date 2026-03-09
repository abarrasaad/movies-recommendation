# 🎬 MovieMind: Vanilla Full-Stack Recommender Engine

A high-performance movie recommendation system built from the ground up. This project demonstrates **Machine Learning** integration, **REST API** handling, and **State Management** without the use of heavy frontend or backend frameworks.

## 🧠 The Engineering Behind the App

### 1. The Recommendation Logic (Python)
Unlike basic "top-rated" lists, this engine uses a **Collaborative Filtering** approach:
* **User-Item Matrix:** Maps thousands of user ratings to movie IDs.
* **Cosine Similarity:** Calculates the mathematical "distance" between users to find "Taste Neighbors."
* **Ghost Profiling:** Dynamically injects a temporary user (the visitor) into the matrix to generate real-time predictions without polluting the primary dataset.

### 2. The Full-Stack Architecture
* **Backend:** Flask (Python) serving as a lightweight REST API.
* **Frontend:** Vanilla HTML5, CSS3 (Grid/Flexbox), and JavaScript.
* **Data Source:** MovieLens Latest-Small dataset (100k+ ratings).
* **Media Integration:** Real-time poster fetching via **TMDB API**.

### 3. Key Technical Challenges Solved
* **Stateless Persistence:** Used `sessionStorage` to allow users to select movies across multiple search results without losing their progress.
* **API Mapping:** Built a "Rosetta Stone" dictionary to map MovieLens IDs to TMDB IDs for image retrieval.
* **Performance Optimization:** Implemented logic to handle API latency during batch requests.*

<img width="1241" height="671" alt="image" src="https://github.com/user-attachments/assets/d4e8fa5e-5685-4192-ab03-078a882d8fe4" />


## 🚀 How to Run Locally

1. **Clone the repo:**

1.  **Install requirements: **
   pip install -r requirements.txt

3.  **Get your TMDB API Key:**
    
    *   Go to [The Movie Database (TMDB)](https://www.themoviedb.org/) and create a free account.
        
    *   Request an API Key (Settings -> API).
        
    *   Rename .env.example to .env and paste your TMDB_API_KEY
  
        
4.  **Run app.py then go to http://127.0.0.1:5000 on your browser**
    

📂 Project Structure
--------------------

*   app.py: The Flask server and REST API routes.
    
*   movie_engine.py: The "Brain" – contains the Collaborative Filtering logic and data ingestion.
    
*   templates/index.html: The Vanilla JS frontend and dynamic UI.
    
*   static/style.css: Custom CSS (Vanilla CSS - No Bootstrap/Tailwind).
    
*   ml-latest-small/: The dataset containing 100,000 ratings.

  

  
    

**Author:** Abarra Saad Eddine

_Data Science Student & Full-Stack Engineer_
