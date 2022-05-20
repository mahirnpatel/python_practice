# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

origList = [12,67, 98, 34]
SummationList=[]

for i in origList:
    sumOfdigit =0
    ld = i % 10
    fd = i/10
    fd = int(fd)
    sumOfdigit = ld + fd
    SummationList.append(sumOfdigit)    

print(SummationList)