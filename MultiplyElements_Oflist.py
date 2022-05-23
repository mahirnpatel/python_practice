# Input :  list1 = [1, 2, 3] 
# Output : 6 
# Explanation: 1*2*3=6 

x=1
numList = [1,2,3]
print(numList)

for i in numList:
    x *= i

print("The Multiplication of element in the list ==> " , x )