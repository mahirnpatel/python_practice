# Input: start = 4, end = 15
# Output: 4, 6, 8, 10, 12, 14

start = int(input("Enter  Starting Range : "))
end = int(input("Enter Ending Range : "))

print("The even numbers ",end="==> ")

for i in range(start , end):
    if(i % 2 == 0 ):
        print(i,end=",")

print("\n")