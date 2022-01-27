def avgTotal(numString):
    list = []
    if numString == "":
        return 0.0
    else:
        for ch in range(0, len(numString)):
            list.append(int(numString[ch]))
    return sum(list) / len(list)


def safeDecoder(characterString):
    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for ch in range(0, len(characterString)):
        if characterString[ch] in list:
            return ch
        else:
            continue


def testScore(test1, test2):
    list1 = []
    list2 = []
    for i in range(0, len(test1)):
        if test1[i] != "_":
            list1.append(int(test1[i]))
    for i in range(0, len(test2)):
        if test2[i] != "_":
            list2.append(int(test2[i]))
    avg_test1 = sum(list1) / len(list1)
    avg_test2 = sum(list2) / len(list2)
    if avg_test1 > avg_test2:
        return avg_test1 * 20
    elif avg_test2 > avg_test1:
        return avg_test2 * 20
    elif avg_test2 == avg_test1:
        return "Same Percentage"


def trip(tripTotalCost, bankBalance, interestRate):
    list = []
    interestRate = interestRate / 100
    while bankBalance < tripTotalCost:
        bankBalance = bankBalance * (1 + interestRate)
        list.append("1")
    num_months = len(list)
    return num_months


def rightTriangles(numRows, character):
    for i in range(0, numRows + 1):
        print(character * i)
