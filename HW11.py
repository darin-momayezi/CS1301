def puppyFinder(puppyCityDict, cityDistanceDict):
    distance = 1000
    closestCity = ''
    myPuppy = ''
    for city in cityDistanceDict:
        if cityDistanceDict[city] < distance:
            closestCity = city
            distance = cityDistanceDict[city]
            
    for puppy in puppyCityDict:
        if puppyCityDict[puppy] == closestCity:
            myPuppy = puppy
            
    return "Your new puppy, {}, is in {} {} miles away.".format(myPuppy, closestCity, distance)

def doubleOddhalfEven(numberList):
    if len(numberList) == 0:
        return []
    else:
        if numberList[0] % 2 == 0:
            return sorted([int(numberList[0] / 2)] + doubleOddhalfEven(numberList[1:]))
        else:
            return sorted([int(numberList[0] * 2)] + doubleOddhalfEven(numberList[1:]))
        
def datingApp(profile1, profile2):
    numCommonInterests = 0
    for interest in profile1[2]:
        if interest in profile2[2]:
            numCommonInterests += 1
            
    interests = []
    for interest in profile1[2]:
        for interest2 in profile2[2]:
            if interest2 not in interests:
                interests.append(interest2)
        if interest not in interests:
            interests.append(interest)
    
    if abs(profile1[1] - profile2[1]) <= 5 and numCommonInterests >= 3:
        ratio = round((numCommonInterests / len(interests) * 100), 1)
        return f"You're {ratio}% compatible!"
    else:
        return "Sorry, you're incompatible." 
    
def simplestDirections(directions):
    '''Up and right definied to be positive directions. Donwn and left negative.'''
    
    upOrDown = 0
    leftOrRight = 0
    for char in directions:
        if char == '<':
            leftOrRight -= 1
        elif char == '>':
            leftOrRight += 1
        elif char == 'U':
            upOrDown += 1
        elif char == 'D':
            upOrDown -= 1
            
    vertical = ''
    horizontal = ''
    if upOrDown <= 0:
        vertical = 'down'
    elif upOrDown >= 0:
        vertical = 'up'
        
    if leftOrRight <= 0:
        horizontal = 'left'
    elif leftOrRight >= 0:
        horizontal = 'right'
    
    if upOrDown == 0 and leftOrRight == 0:
        return "No movement."
    else:
        return f"You have moved {abs(upOrDown)} blocks {vertical} and {abs(leftOrRight)} blocks {horizontal}."
     
def songMystery(codedSong, songNames):
    most = 0
    newSong = ''
    for song in songNames:
        common = 0
        for char in codedSong.lower():
            if char in song.lower():
                common += 1
        if common > most:
            most = common
            newSong = song
    if len(newSong) == most and newSong != 'red':
        return newSong.lower()
    else:
        return "I need more clues :("    
