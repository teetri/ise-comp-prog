def _p(x):
    for i in x:
        print(i)
        print()


def _pl(x):
    for i in x:
        for j in i:
            print(j)
        print()


def _pd(x):
    for i in x:
        for j, k in i.items():
            print(j, k)
        print()


lines = ['HSET "movie:1" title "Guardians of the Galaxy" genre "Action" votes 704613 rating 8.1 release_year 2014 plot "A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe." poster "https://m.media-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SX300.jpg" ibmdb_id "tt2015381" \n',
         'HSET "movie:2" title "Interstellar" genre "Adventure" votes 961763 rating 8.6 release_year 2014 plot "A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival." poster "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg" ibmdb_id "tt0816692" \n',
         'HSET "movie:7" title "X-Men: Days of Future Past" genre "Action" votes 524078 rating 8.0 release_year 2014 \n',
         'HSET "movie:297" title "Pod livnem pul" genre "Drama" votes 33 rating 6.6 release_year 2006  plot "Crimea Ukraine ca 1942. WWII. An elite squad of \\"razvedchiks\\" - army scouts - is sent deep behind German lines on a series of dangerous but vital reconnaissance missions for the Red Army." poster "https://m.media-amazon.com/images/M/MV5BNDlkZmUwMGEtMTJmNC00ODlmLTk3NjYtMDc1MjViOWRlM2YxXkEyXkFqcGdeQXVyNjExMjE5OTM@._V1_SX300.jpg" ibmdb_id "tt0902116"']

f = open('movies_full.txt', 'r')
lines = f.readlines()
# lines = [line for line in lines if '1007' in line]
# print(lines[1])
# lines = [lines[1]]
f.close()


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

# _p(movies.items())

print(movies)
