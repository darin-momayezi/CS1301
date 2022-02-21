from calendar import weekday

def counterPick(fighter):
    counter = {
            'mario':['luigi','link'],
            'luigi':['bowser','ness'],
            'bowser':['mario','link'],
            'captain falcon':['fox','marth'],
            'fox':['samus','mewtwo'],
            'ness':['bowser','samus'],
            'kirby':['mario','captain falcon'],
            'samus':['pikachu','marth'],
            'link':['fox','ness'],
            'pikachu':['captain falcon','kirby'],
            'marth':['luigi','mewtwo'],
            'mewtwo':['kirby','pikachu']
    }
    return counter.get(fighter)


def showToWatch(friendsFavShows, favoriteShow):
    friends = []
    for a in friendsFavShows:
        if favoriteShow in a[1]:
            friends.append(a[0])
    return friends


def fixLabels(labelList):
    corrected = []
    names = []
    prices = []
    index = 0
    for element in labelList:
        if type(element) == str:
            names.append(element)
        elif type(element) == float:
            prices.append(element)

    for element in names:
        corrected.append((element, prices[index]))
        index += 1
    return sorted(corrected)


def newPlaylist(playlist):
    songs = []
    mins = []
    secs = []
    for element in playlist:
        songs.append(element[0])
        mins_secs = element[1].split(':')
        mins.append(float(mins_secs[0]))
        secs.append(float(mins_secs[1]))
    return [tuple(sorted(songs)), (sum(mins) + (sum(secs) / 60))]


def birthdays(friends, birthdates):
    listOfNames = []
    index = 0
    for element in birthdates:
        if 4 < weekday(year=2022, month=element[0], day=element[1]):
            listOfNames.append(friends[index])
        index += 1
    return sorted(listOfNames)


def smashBros(fighterList, opponents):
    goodPicks = []
    if counterPick(opponents) in fighterList:
        goodPicks.append(counterPick(opponents))
    return goodPicks
