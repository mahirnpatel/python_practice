user_input = int(input("Enter size : "))
i = 0
j = 0

# for i in range(user_input+1):
#     for j in range(i):
#         print("* ", end=" ")
#     print('')

# for i in range(user_input , i):
#     for j in range(i):
#         print("* ",end=" ")
#     print("")

for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print('')


for i in range(user_input, 0, -1):  # -1 for decrementing the loop 
    print("The value of i ", i)
    for j in range(i):
        print("The value of j ", j)
        print('* ', end="")
    print('')
