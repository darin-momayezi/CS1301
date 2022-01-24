def workout(exerciseName, interestedFriends, totalFriends):
    if (interestedFriends / totalFriends) < 0.2:
        print("Let's try a different workout.")
    if 0.2 <= (interestedFriends / totalFriends) < 0.7:
        print(f"We will try to {exerciseName} for 30 minutes.")
    if (interestedFriends / totalFriends) >= 0.7:
        print(f"We're so excited to {exerciseName}!")


def iceCream(rating, distance):
    if rating == 4.5 and distance == 7.5:
        choice = "Jeni's"
        return choice
    elif rating == 4.5 and distance == 3.6:
        choice = "Cold Stone"
        return choice
    elif rating == 4.5 and distance == 4.2:
        choice = "Morelli's"
        return choice
    elif rating == 4.0 and distance == 1.3:
        choice = "Bruster's"
        return choice
    elif rating == 4.0 and distance == 6.4:
        choice = "Sweet Stack"
        return choice
    elif rating == 3.5 and distance == 2.8:
        choice = "Baskin Robbins"
        return choice
    else:
        return "Try again tomorrow."


def restaurantDecider(veganFriendly, yelpStars, milesAway):
    if not veganFriendly:
        return "Not tonight."
    elif veganFriendly == True and yelpStars < 3:
        return "Not good enough food."
    elif veganFriendly == True and yelpStars >= 3 and milesAway > 5:
        return "Too far!"
    elif veganFriendly == True and yelpStars >= 3 and milesAway <= 5:
        return "Perfect restaurant!"


def dinnerTip(numFriends, dinnerCost):
    if numFriends <= 3:
        tipAmount = 0.15 * dinnerCost
        return round(tipAmount, 2)
    elif 3 < numFriends <= 7:
        tipAmount = 0.2 * dinnerCost
        return round(tipAmount, 2)
    elif numFriends > 7:
        tipAmount = 0.25 * dinnerCost
        return round(tipAmount, 2)


def planMaker(timeA, costA, timeB, costB):
    if costA < costB:
        return "planA"
    elif costB < costA:
        return "planB"
    elif timeA < timeB:
        return "planA"
    elif timeB < timeA:
        return "planB"
    else:
        return "No plans this weekend."
