import math

## Begin functions
# dinstance of two objects [USING EUCLIDEAN DISTANCE]
def euclideanDistance(obj1, obj2):
    eucSum = 0
    for o1, o2 in zip(obj1, obj2):
        eucSum += (o1 - o2)**2
    return round(math.sqrt(eucSum), 5)

# dinstance of two objects [USING CHEBYSHEV DISTANCE]
def chebyshevDistance(obj1, obj2):
    resCheby = []
    for o1, o2 in zip(obj1, obj2):
        resCheby.append(abs(o1 - o2))
    return max(resCheby)

# function that finds the distance between objects
def objDistanceFun(objsList):
    tempList = []
    for i in range(len(objsList)):
        deltaList = []
        for j in range(len(objsList)):
            deltaList.append(euclideanDistance(objsList[i], objsList[j]))
            #deltaList.append(chebyshevDistance(objsList[i], objsList[j]))
        tempList.append(deltaList)
    return tempList

# k the min closet, return list
def kMinList(k, objsDistance):
    i = 0 # current obj
    tempDistance = [row[:] for row in objsDistance] # copy objDistance
    resultList = [] # current obj, k min the closet, distance
    for tempRow, row in zip(tempDistance, objsDistance):
        tempRow.sort()
        resultList.append([i, row.index(tempRow[k]), round(1.0 / tempRow[k], 5)])
        i+=1
    return resultList

# Final function 
def finalFun(resList):
    EndMax = resList[0][0]
    EndIndex = 0
    EndKIndex = 0
    for i in range(len(resList)):
        if EndMax < resList[i][2]:
            EndMax = resList[i][2]
            EndIndex = i
            EndKIndex = resList[i][1]
    return EndIndex, EndKIndex, EndMax

# demonstrating 2DList
def print2DList(tempList):
    for row in tempList:
        for item in row:
            print(item, end="\t")
        print()
    print("*****************************************************")

## End functions

# read from file
with open("myObjectsFile.txt") as f:
    objsList = [[float(value) for value in line.split(" ")] for line in f]

objsDistance = objDistanceFun(objsList)

k = int(input("Enter number:"))
resList = kMinList(k, objsDistance)

EndIndex, EndKIndex, EndMax = finalFun(resList)
print(f"{EndIndex+1} ---> {EndKIndex+1} ---> {EndMax}")

