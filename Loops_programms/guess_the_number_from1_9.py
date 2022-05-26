guessedNumber = 5
userGuess = 0

while(True):
    userGuess = int(input("Guess the number : "))

    if(userGuess == guessedNumber):
        print("Well Guessed , you win the game")
        break;
    else:
        print("Wrong guess")

    print("\n")    