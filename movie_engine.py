import csv
import math

movie_nodes = {}
tmdb_map = {}

with open('ml-latest-small/links.csv', newline='', encoding='utf-8') as csvfile:
    tmdb = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(tmdb)
    for row in tmdb:
        if row[2]:
            movie_id = int(row[0])
            tmdb_id = int(row[2])
            tmdb_map[movie_id] = tmdb_id


with open('ml-latest-small/movies.csv', newline='', encoding='utf-8') as csvfile:
    movies = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(movies)
    for row in movies:
        movie_id = int(row[0])
        movie_nodes[movie_id] = {"movie_id": movie_id, "title": row[1], "genre": row[2], "tmdb_id": tmdb_map.get(movie_id)}

user_ratings = {}

with open('ml-latest-small/ratings.csv', newline='', encoding='utf-8') as csvfile:
    ratings = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(ratings)
    for row in ratings:
        user_id = int(row[0])
        movie_id = int(row[1])
        rating = float(row[2])
        if user_id not in user_ratings:
            user_ratings[user_id] = {}
        user_ratings[user_id][movie_id] = rating


def calculate_similarity(user1, user2):
    user1_movies = set(user_ratings[user1])
    user2_movies = set(user_ratings[user2])
    similar = user1_movies.intersection(user2_movies)
    if not similar:
        return 0.0
    top_product = sum(user_ratings[user1][movie] * user_ratings[user2][movie] for movie in similar)
    magnitude1 = math.sqrt(sum(rating**2 for rating in user_ratings[user1].values()))
    magnitude2 = math.sqrt(sum(rating**2 for rating in user_ratings[user2].values()))
    
    return top_product / (magnitude1 * magnitude2)

def get_top_neighbors(target_user, top_n=5):
    similarities = []
    for user in user_ratings:
        if (user == target_user):
            continue
        score = calculate_similarity(target_user, user)
        similarities.append((user, score))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

def recommend_movies(target_user, num_recommendations = 5):
    neighbors = get_top_neighbors(target_user, 50)
    movies_score = {}
    similarity_sums = {}
    for neighbor, sim_score in neighbors:
        for movie, rating in user_ratings[neighbor].items():
            if movie in user_ratings[target_user]:
                continue
            if movie not in movies_score:
                movies_score[movie] = 0.0
                similarity_sums[movie] = 0.0
            movies_score[movie] += (rating * sim_score)
            similarity_sums[movie] += sim_score
    predictions = []
    for movie in movies_score:
        if similarity_sums[movie] > 0: 
            predicted_rating = movies_score[movie] / similarity_sums[movie]
            predictions.append((movie, predicted_rating))
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_titles = []
    for movie_tuple in predictions[:num_recommendations]:
        top_titles.append(movie_nodes[movie_tuple[0]]["title"])
    return top_titles
