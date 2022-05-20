# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

numList=[23,65,19,90]
print("INPUT ==> " , numList)
pos1=int(input("Enter the first position : "))
pos2=int(input("Enter the Second position : "))

tmp = numList[pos2]
numList[pos2] = numList[pos1]
numList[pos1] = tmp

print("OUTPUT ==> " , numList)
