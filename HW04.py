def messageDecoder(message):
    decoded = ""
    for char in message:
        if char.isalpha():
            decoded += str(char)
        elif char.isdigit():
            continue
        elif char == " ":
            decoded += " "

    return decoded[::-1]


def clubMembers(interested, recruits):
    memberList = []
    for i in interested:
        memberList.append(i)
    for i in recruits:
        if i in interested:
            continue
        else:
            memberList.append(i)
    return memberList


def checkCareer(students, career):
    selectedStudents = []
    for i in students:
        if i[1] == career:
            selectedStudents.append(i[0])
    return sorted(selectedStudents)


def highGrades(students, gpas):
    honorsStudents = []
    index = 0
    for i in gpas:
        index += 1
        if i >= 3.5:
            honorsStudents.append(students[index - 1])
    return honorsStudents


def quidditchPlay(playerOrder, partners):
    isApproved = False
    for i in range(len(playerOrder)):
        if playerOrder[i] in partners and playerOrder[i + 1] in partners:
            isApproved = True
            return isApproved
        elif i != 0 and playerOrder[i] in partners and playerOrder[i - 1] in partners:
            isApproved = True
            return isApproved
    return isApproved
