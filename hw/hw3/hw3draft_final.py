import pandas as pd
from collections import OrderedDict
f = open('movies_full.txt', 'r')
lines = f.readlines()
f.close()

# MOVIE_DICTIONARY (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main().


def load_data_to_movie_dict(lines):
    movies = dict()
  # Your code here

    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    keySep = {
        'movie_id': '|movie_id^',
        ' title ': '|title^',
        ' genre ': '|genre^',
        ' votes ': '|votes^',
        ' rating ': '|rating^',
        ' release_year ': '|release_year^',
        ' plot ': '|plot^',
        ' poster ': '|poster^',
        ' ibmdb_id ': '|ibmdb_id^'
    }

    def cleanLine(line):
        line = line.replace('HSET ', '')
        line = line.replace('movie:', 'movie_id')
        line = line.replace('"', '')
        line = line.replace('\\', '')
        line = replace_all(line, keySep)
        line = line.split('|')
        return line

    def toPairs(line):
        pairs = []
        for i in line:
            if i != '':
                pairs.append(i.split('^'))
        return pairs

    def toDict(pairs):
        d = {}
        # print()
        for i in pairs:
            # print(i)
            # print(i[0].strip(), i[1].strip())
            # print()
            d[i[0].strip()] = i[1].strip()
        return d

    def toCorrectType(line):
        try:
            line['movie_id'] = int(line['movie_id'])
        except:
            pass
        try:
            line['votes'] = float(line['votes'])
        except:
            pass
        try:
            line['rating'] = float(line['rating'])
        except:
            pass
        try:
            line['release_year'] = int(line['release_year'])
        except:
            pass
        return line

    def parseLine(line):
        line = cleanLine(line)
        # print(line)
        # print()
        line = toPairs(line)
        # print(line)
        # print()
        line = toDict(line)
        # print(line)
        # print()
        line = toCorrectType(line)
        # print(line)
        # print()

        return line

    lines = [parseLine(line) for line in lines]

    def removeMovieID(d):
        return {k: v for k, v in d.items() if k != 'movie_id'}

    movies = {a['movie_id']: removeMovieID(a) for a in lines}

    return movies

#------------------------------------------------------------#


def summarize_movies_by_genre(movies):
    movies_by_genre = dict()
    # Your code here

    genres = dict()
    for movie in movies:
        genre = movies[movie]['genre']
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(movie)

    movies_by_genre = genres

    return movies_by_genre

#------------------------------------------------------------#


def calcualte_genre_stats(movies, movies_by_genre):
    genre_stats = dict()
    # Your code here
    #   genre_stats = dict()
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

    return genre_stats

#------------------------------------------------------------#
# DO NOT DELETE OR MODIFIED THE CODE BELOW
#------------------------------------------------------------#


# print "data" dict ordered by key
# if top is blank, print all members in the data
# if details is true, print detailed data
#   ; otherwise, print only the number of attributes


def print_ordered_dict(data, top='', details=True):
    if top == '':
        top = len(data)
    sorted_ids = sorted(data.keys())[:top]

    i = 0
    for id in sorted_ids:
        if details:
            print(id, data[id])
        else:
            print(id, len(data[id]))


#------------------------------------------------------------#
# *** MAIN PART ****
movies = load_data_to_movie_dict(lines)
movies_by_genre = summarize_movies_by_genre(movies)
genre_stats = calcualte_genre_stats(movies, movies_by_genre)


print(len(movies))
# print attributes (Google Sheet1)
# print_ordered_dict(data=movies, top=200, details=False)
# print data (Google Sheet2)
# print_ordered_dict(data=movies, top=1141, details=True)

print(len(movies_by_genre))
# print attributes (Google Sheet3)
# print_ordered_dict(data=movies_by_genre, top=5, details=False)
# print_ordered_dict(data=movies_by_genre, top=5)  # print data (Google Sheet4)
# print_ordered_dict(data=genre_stats, top=5)  # print data (Google Sheet5)


# d = {'Apple': {'Weight': 12, 'Colour': 'red'},
#      'Banana': {'Weight': 11, 'Colour': 'yellow', 'Bunched': 1}
#      }

# convert dict to dataframe
df = pd.DataFrame.from_dict(genre_stats, orient='index')

df.to_csv('genre_stats.csv')  # write dataframe to file
