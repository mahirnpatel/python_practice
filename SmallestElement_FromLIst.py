# Input : list1 = [10, 20, 4]
# Output : 4

numList = [10, 20, 4]

print(numList)

x = numList[0]
print(x)

for i in numList:
    if(x > i):
        x = i

print(x)
