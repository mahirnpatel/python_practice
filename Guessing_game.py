import random  #IMPORTING THE RANDOM MODULE 

rangeOfNumbers = int(input("Enter the range : "))  #TAKE THE RANGE  OF THE NUMBER FROM THE USER

randomNum = random.randint(1,rangeOfNumbers)  #GENRATE THE NUMBER WHICH IS NOT GREATER THAN THE USER GIVEN NUMBER

numberOfguess = 0 #THIS COUNTER STORE THE NUMBER OF GUESS TAKEN BY THE USER

outofRange = False  #THIS IS FOR CHECKING THE GIVEN NUMBER IS IN RANGE OR NOT

print('\t\t-------------------------Game Start-------------------------')
print(f"\n\n\t\t\tYou have to guess the number between 1 - {rangeOfNumbers}")

user_num = int(input("\n\nEnter num : "))

#IF THE USER NUMBER IS GREATRER THAN RANGE GIVEN BY THE USER ITSELF THAN PRINT THE WARNING
if(user_num > rangeOfNumbers):
    print("Warning : You cannot enter the number of out of range,please restart the game and again enter the range")

#ELSE START THE GAME
else:

    last_guessedNumber = user_num

    while(user_num != randomNum):

        
        if(user_num > rangeOfNumbers):

               print("Warning : You cannot enter the number of out of range,please restart the game and again enter the range") 

               outofRange = True

               break
        else:

            #IF THE USER NUMBER IS GREATER THAN THE RANDOM NUMBER THAN GIVE USER THE HINT TO GUESS THE LEAST NUMBER THAN CURRENT NUMBER
            if(user_num > randomNum):
                print("The last guessed number : " , last_guessedNumber)
                user_num=int(input("Guess Lower digit number than last one : "))
                last_guessedNumber = user_num

                numberOfguess += 1

            #IF THE USER NUMBER IS SMALLER THAN THE RANDOM NUMBER THAN GIVE USER THE HINT TO GUESS THE HIGH NUMBER THAN CURRENT NUMBER
            elif(user_num < randomNum):
                print("The last guessed number : " , last_guessedNumber)
                user_num=int(input("Guess Higher digit number than last one : "))
                last_guessedNumber = user_num
                numberOfguess += 1
            
        print("\n\t\t------------------------------------------------------\n")

    if(outofRange == False):
        print(f"\t\tCongratulations , You won the game by guessing {numberOfguess} times\n\n")