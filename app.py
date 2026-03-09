import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
import movie_engine
import requests

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def fetch_poster(tmdb_id):
    if not tmdb_id:
        return "https://via.placeholder.com/200x300?text=No+Poster"

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"
    response = requests.get(url).json()
    
    poster_path = response.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/200x300?text=No+Poster"


app = Flask(__name__)

@app.route('/')
def home():
    search_word = request.args.get('query')
    all_movies = list(movie_engine.movie_nodes.values())
    
    if search_word:
        search_word = search_word.lower()
        movies = [m for m in all_movies if search_word in m['title'].lower()]
    else:
        movies = all_movies[:50]

    for movie in movies:
        movie['poster_url'] = fetch_poster(movie.get('tmdb_id'))
        
    return render_template('index.html', movies=movies)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    user_picks = data['ghost_profile']
    ghost_id = 999999
    
    movie_engine.user_ratings[ghost_id] = {}
    for movie_id in user_picks:
        movie_engine.user_ratings[ghost_id][movie_id] = 5.0
        
    predicted_titles = movie_engine.recommend_movies(ghost_id)
    
    del movie_engine.user_ratings[ghost_id]


    results_with_posters = []
    for title in predicted_titles:
        movie_node = next((m for m in movie_engine.movie_nodes.values() if m['title'] == title), None)
        
        poster_url = ""
        if movie_node:
            poster_url = fetch_poster(movie_node.get('tmdb_id'))
            
        results_with_posters.append({
            "title": title,
            "poster": poster_url
        })
        
    return jsonify({"recommendations": results_with_posters})
    
if __name__ == '__main__':
    app.run(debug=True)