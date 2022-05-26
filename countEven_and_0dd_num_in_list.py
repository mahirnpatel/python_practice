# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2

numList = [1,2,3,4,5,6,7,8,9,10,45]
evenCounter=0
oddCounter=0

for i in numList:
    if(i%2 == 0):
        evenCounter += 1
    else:
        oddCounter += 1    

print("The number of even elements ==> ", evenCounter)
print("The number of odd elements ==> ", oddCounter)