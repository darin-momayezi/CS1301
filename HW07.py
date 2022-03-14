def featureActor(filename, actorName):
    movies = open(str(filename), 'r')
    features = movies.readlines()
    movies.close()
    movieList = []
    index = 0
    for element in features:
        if actorName + "\n" == element:
            movieList.append(features[index - 1].replace('\n', ''))
        index += 1
    if len(movieList) == 0:
        return "Actor not found"
    else:
        return movieList


def alphabetSearch(filename, letter):
    movieDict = {}
    movies = open(str(filename), 'r')
    features = movies.readlines()
    movies.close()
    for index in range(2, len(features), 4):
        if features[index][0].lower() == letter:
            movieDict[features[index].replace('\n', '')] = features[index + 1].replace('\n', '')
    return movieDict


def favFilms(filename, movieList):
    allMovies = open(filename, 'r')
    allMovieInfo = allMovies.readlines()
    allMovies.close()
    movieDict = {}
    for index in range(2, len(allMovieInfo), 4):
        if allMovieInfo[index].replace('\n', '') in movieList:
            movieDict[allMovieInfo[index].replace('\n', '')] = [allMovieInfo[index + 1].replace('\n', ''),
                                                                allMovieInfo[index + 2].replace('\n', '')]
    favMovies = open('favMovies.txt', 'w')
    favMovies.write('Movie Data\n')
    index = 0
    for movie in movieDict.keys():
        favMovies.write('\n')
        favMovies.write(str(movie) + '\n')
        favMovies.write(str(movieDict[movie][0]) + '\n')
        if (index + 1) == len(movieDict.keys()):
            favMovies.write(str(movieDict[movie][1]))
        else:
            favMovies.write(str(movieDict[movie][1] + '\n'))
        index += 1
    favMovies.close()


def movieNight(filename, timeLimit):
    movieData = {}
    movieFile = open(filename, 'r')
    data = movieFile.readlines()

    for index in range(1, len(data)):
        movieInfo = data[index].split(',')
        movie = movieInfo[0]
        imdb = int(movieInfo[1])
        rotten = int(movieInfo[2])
        time = int(movieInfo[3].replace('\n', ''))
        avg = (imdb + rotten) / 2
        movieData[movie] = [avg, time]
    movieFile.close()

    possibilities = []
    for movie in movieData.keys():
        if movieData[movie][1] <= timeLimit:
            possibilities.append((movie, movieData[movie][0]))

    highest = 0
    choice = ''
    for element in possibilities:
        if element[1] >= highest:
            highest = element[1]
            choice = element[0]
    return (choice, highest)


def movieRecs(filename, interestedList, expectedRatio):
    movieData = {}
    movieFile = open(filename, 'r')
    data = movieFile.readlines()
    reccomendations = {}

    for index in range(1, len(data)):
        movieInfo = data[index].split(',')
        movie = movieInfo[0]
        imdb = int(movieInfo[1])
        rotten = int(movieInfo[2])
        time = int(movieInfo[3].replace('\n', ''))
        avg = (imdb + rotten) / 2
        movieData[movie] = [avg, time]
    movieFile.close()

    for movie in movieData.keys():
        movieData[movie] += [movieData[movie][0] / movieData[movie][1]]

    for movie in movieData.keys():
        if movie in interestedList and movieData[movie][2] >= expectedRatio:
            reccomendations[movie] = movieData[movie][1]

    if len(reccomendations) == 0:
        return 'Too many expectations'
    else:
        return reccomendations
