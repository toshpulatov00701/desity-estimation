import numpy as np
import math

## Begin functions

# dinstance of two objects [USING EUCLIDEAN DISTANCE]
def euclideanDistance(data):
    for i in range(len(data)):
        for j in range(len(data)):
            distance_matrix[i, j] = np.round(np.sqrt(np.sum((data[i][:len(data[0])] - data[j][:len(data[0])])**2)), 2)
            distance_matrix[j, i] = distance_matrix[i, j]
    return distance_matrix

# dinstance of two objects [USING CHEBYSHEV DISTANCE]
def chebyshevDistance(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            distance_matrix[i, j] = np.max(np.abs(data[i][:len(data[0])] - data[j][:len(data[0])]))
            distance_matrix[j, i] = distance_matrix[i, j]
    return distance_matrix

# final function
def finalFun(distance_matrix, k):
    sorted_rows = np.sort(distance_matrix)
    selectedCol = sorted_rows[0:len(data),k]
    minValue = np.min(selectedCol)
    endIndex = np.argmin(selectedCol)
    endKIndex = np.where(distance_matrix[endIndex] == minValue)[0][0]
    return 1.0 / minValue, endIndex, endKIndex

# demonstrating 2DList
def print2DList(tempList):
    for row in tempList:
        for item in row:
            print(item, end="\t")
        print()
    print("*****************************************************")

## End functions

data=np.loadtxt('myObjectsFile.txt',dtype=float)

distance_matrix = np.zeros((len(data), len(data)))

distance_matrix = euclideanDistance(data)
#distance_matrix = chebyshevDistance(data)

k = int(input("Enter number:"))
result = finalFun(distance_matrix, k)

print(f"{result[1] + 1} -- {result[2] + 1} -- {result[0]}")