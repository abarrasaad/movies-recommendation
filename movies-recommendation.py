import csv

movie_nodes = {}

with open('ml-latest-small\movies.csv', newline='', encoding='utf-8') as csvfile:
    movies = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(movies)
    for row in movies:
        movie_id = int(row[0])
        movie_nodes[movie_id] = {"movie_id": movie_id, "title": row[1], "genre": row[2]}

user_ratings = {}

with open('ml-latest-small\\ratings.csv', newline='', encoding='utf-8') as csvfile:
    ratings = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(ratings)
    for row in ratings:
        user_id = int(row[0])
        movie_id = int(row[1])
        rating = float(row[2])
        if user_id not in user_ratings:
            user_ratings[user_id] = {}
        user_ratings[user_id][movie_id] = rating

print(user_ratings[1])