numList1=[1,2,3,4,2,4,5,3]
tmp = []
counter=0
for i in numList1:
    if(i not in tmp):
        counter += 1
        tmp.append(i)

print("The unique values are ==> ",tmp)