# Input ==>  [1, 2, 3, 5, 6, 24]
# OUTPUT ==>  [24, 2, 3, 5, 6, 1]

numList = [1,2,3,5,6,24]
print("Input ==> ",numList)

lengthOfList=len(numList)

tmp = numList[lengthOfList-1]
numList[lengthOfList-1] = numList[0];
numList[0] = tmp

print("OUTPUT ==> " , numList)
