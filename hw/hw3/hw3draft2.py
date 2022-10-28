from hw3data_all import movies

# print(type(movies))


def summarize_movies_by_genre(movies):
    genres = dict()
    for movie in movies:
        genre = movies[movie]['genre']
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(movie)
    # print(genres)
    return genres


def calcualte_genre_stats(movies, movies_by_genre):
    genre_stats = dict()
    for genre in movies_by_genre:
        genre_stats[genre] = dict()
        count = len(movies_by_genre[genre])
        avg_rating = 0
        avg_votes = 0
        for movie in movies_by_genre[genre]:
            # print(type(movies[movie]['rating']))
            # print(movie)
            avg_rating += movies[movie]['rating']
            avg_votes += movies[movie]['votes']
        avg_rating /= count
        avg_votes /= count
        genre_stats[genre]['num'] = count
        genre_stats[genre]['rating'] = round(avg_rating, 2)
        genre_stats[genre]['votes'] = round(avg_votes, 2)

    # print(genre_stats)
    return genre_stats


print(calcualte_genre_stats(movies, summarize_movies_by_genre(movies)))
