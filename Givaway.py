import random
print("First enter the delimiter seperating the names (they have to all be on the same line)\nThen enter the names of the entrants\nThen enter the prize delimiter\nThen enter the prizes\n")
entrantDelimiter = input("Enter the name delimiter (what character(s) divides the names)\n")
entrantNames = input("Enter the entrant names (all on the same line, divided by the delimiter you previously specified)\n")
entrantList = list(entrantNames.split(entrantDelimiter))
prizeDelimiter = input("Enter the name delimiter (what character(s) divides the prizes)\n")
prizeNames = input("Enter the prize names (all on the same line, divided by the delimiter you previously specified)\n")
prizeList = list(prizeNames.split(prizeDelimiter))
if len(entrantList) > len(prizeList):
    x = len(entrantList) - len(prizeList)
    for i in range(0, x):
        prizeList.append("Empty Prize")
random.shuffle(entrantList)
random.shuffle(prizeList)
for i in range(0, entrantnum):
    print(entrantList[i]+" has won " + prizeList[i] + "\n")
