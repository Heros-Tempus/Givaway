import random
class NotPositiveError(UserWarning):
    pass
print("First enter the number of entrants\nThen enter the names of the entrants one at a time\nThen enter the number of prizes\nThen enter the prizes one at a time")
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
entrantDelimiter = input("Enter the name delimiter (what character(s) divides the names)\n")
entrantNames = input("Enter the entrant names (all on the same line, divided by the delimiter you previously specified)\n")
entrantList = list(entrantNames.split(entrantDelimiter))
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
prizeDelimiter = input("Enter the name delimiter (what character(s) divides the prizes)\n")
prizeNames = input("Enter the prize names (all on the same line, divided by the delimiter you previously specified)\n")
prizeList = list(prizeNames.split(prizeDelimiter))
if len(entrantLize) > len(prizeLizt):
    x = len(entrantList) - len(prizeList)
    for i in range(0, x):
        prizeList.append("Empty Prize")
random.shuffle(entrantList)
random.shuffle(prizeList)
for i in range(0, entrantnum):
    print(entrantList[i]+" has won " + prizeList[i] + "\n")
