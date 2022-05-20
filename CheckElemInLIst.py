from http.client import NON_AUTHORITATIVE_INFORMATION


numList=[1,4,8,7,6,10,54,100]

numForSearch = int(input("Enter number for search : "))

for x in numList:
    flag =0
    if(x == numForSearch):
        print("Element found in the list")
        break;
    else:
        flag =1    

if(flag == 1):
    print("Element not found ")