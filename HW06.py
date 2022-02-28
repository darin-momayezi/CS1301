def findTicket(ticketDictionary):
    prices = []

    if len(ticketDictionary.items()) == 0:
        return "No tickets available!"

    for airline, cost in ticketDictionary.items():
        prices.append(cost)
        cheapest = sorted(prices)[0]

    for airline, cost in ticketDictionary.items():
        if cost == cheapest:
            return (airline, cost)


def findHotel(hotelDictionary):
    if len(hotelDictionary) == 0:
        return "No hotels available!"

    votes = {}
    hotels = hotelDictionary.values()

    for friend, hotel in hotelDictionary.items():
        num = 0
        for element in hotels:
            if element == hotel:
                num += 1
        votes[str(hotel)] = num

        for hotel, num in votes.items():
            most = sorted(votes.values())[-1]
            if num == most:
                return {hotel: num}


def findEvent(myInterests, schedule):
    match = []

    for date, events in schedule.items():
        for event in events:
            if event in myInterests and date not in match:
                match.append(date)

    return sorted(match)


def figureSkating(technicalScores, componentScores):
    index = 0
    finalScores = []
    for technicalScore in technicalScores:
        try:
            finalScore = technicalScore + componentScores[index]
            finalScores.append(finalScore)
            index += 1
        except TypeError:
            index += 1
        finally:
            pass

    return finalScores


def sportManagement(countryDict):
    sportDict = {}
    for country, sports in countryDict.items():
        for sport in sports:
            if sport not in sportDict.keys():
                sportDict[str(sport)] = []
            if country not in sportDict[str(sport)]:
                sportDict[str(sport)].append(country)

    for sport, countries in sportDict.items():
        sportDict[sport] = sorted(countries)

    return sportDict

