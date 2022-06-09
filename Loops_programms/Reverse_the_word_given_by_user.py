UserString  = input("Enter String ==> " )

print("Input string ==> " , UserString)
i=0

print("Reversed String " , end="==>")
while i<len(UserString):
    print(UserString[len(UserString)-1-i],end="")
    i = i +1
    
print("\n")