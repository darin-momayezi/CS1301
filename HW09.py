def pageNumbers(bookList):
    pageCount = 0
    if len(bookList) <= 1:
        return bookList[0]
    else:
        pageCount += bookList[0]
        return pageCount + pageNumbers(bookList[1:])


def letterPyramid(letter, rows):
    if letter.isupper():
        pass
    elif rows == 1:
        print(letter)
    else:
        letterPyramid(letter, rows - 1)
        print(letter * rows)


def specialChar(usernames):
    count = 0
    symbols = ['.', '-', '_', '!', '~', '#']

    if len(usernames) == 0:
        return {}
    else:
        for symbol in symbols:
            count += usernames[0].count(symbol)
        priorDict = specialChar(usernames[1:])
        priorDict[usernames[0]] = count
        return priorDict


def messageDecoder(hiddenMessage, characters):

    if len(characters) == 0:
        return hiddenMessage
    else:
        newMessage = hiddenMessage.replace(characters[0], '')
        return messageDecoder(newMessage, characters[1:])


def stringCombiner(stringList):

    combinedString = ''

    if len(stringList) == 0:
        return combinedString

    elif type(stringList[0]) != str:
        combinedString += stringList[0][0]
        return combinedString + stringCombiner(stringList[:][1:])
    else:
        combinedString += stringList[0]
        return combinedString + stringCombiner(stringList[1:])
