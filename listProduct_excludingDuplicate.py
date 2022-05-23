# INPUT : numList=[1,3,5,6,3,5,6,1]
# OUTPUT : 90

numList=[1,3,5,6,3,5,6,1]
tmpList=[]
prod=1

for i in numList:
    if(i not in tmpList):
        tmpList.append(i)

for i in tmpList:
    prod *= i

print("The product of the element excluding the duplicate elements ==> " , prod)