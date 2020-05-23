import random
class NotPositiveError(UserWarning):
    pass
print("First enter the number of entrants\nThen enter the names of the entrants one at a time\nThen enter the number of prizes\nThen enter the prizes one at a time")
entrantNames = []
while True:
    try:
        entrantnum = int(input("Enter the number of entrants\n"))
        if entrantnum < 0:
            raise NotPositiveError
    except ValueError:
        print("Not a positive integer.\n")
        continue
    except NotPositiveError:
        print("Not a positive integer.\n")
        continue
    else:
        break
for i in range(0, entrantnum):
    entrantNames.append(input("Enter the name of entrant number " + str(i+1) + "\n"))
prizeNames = []
while True:
    try:
        prizenum = int(input("Enter the number of prizes\n"))
        if prizenum < 0:
            raise NotPositiveError
    except ValueError:
        print("Not a positive integer.\n")
        continue
    except NotPositiveError:
        print("Not a positive integer.\n")
        continue
    else:
        break
for i in range(0, prizenum):
    prizeNames.append(input("Enter the name of prize number " + str(i+1) + "\n"))
if len(entrantNames) > len(prizeNames):
    x = len(entrantNames) - len(prizeNames)
    for i in range(0, x):
        prizeNames.append("Empty Prize")
random.shuffle(entrantNames)
random.shuffle(prizeNames)
for i in range(0, entrantnum):
    print(entrantNames[i]+" has won " + prizeNames[i] + "\n")
