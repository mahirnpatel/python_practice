import random

#THIS IS THE FUNCTION WHICH RETRUN TRUE IF THE USER WINS OR RETRUN FALSE IF COMPUTER WINS 
def gameBegins(comp, userChoice):
    if(comp == userChoice):
        return None

    if(comp == 's'):
        if(userChoice == 'p'):
            return False

    if(comp == 'p'):
        if(userChoice == 's'):
            return True

    if(comp == 's'):
        if(userChoice == 'sc'):
            return False

    if(comp == 'sc'):
        if(userChoice == 's'):
            return True

    if(comp == 'p'):
        if(userChoice == 'sc'):
            return True

    if(comp == 'sc'):
        if(userChoice == 'p'):
            return False

#take input of how much time wants to play the game 
numOfTimes = int(input("How many times you want to play the Game ? : "))
noOfRounds =1 #MAKE counter VARIABLE FOR SHOWING THE ROUNDS
highScore  = 0  #THIS WILL STORE THE CURRENT SCORE

while(numOfTimes > 0):
    print("\n\t\t----------------Round", noOfRounds , end=" Begins------------------")
    print("\n\nComputer Selected,please select your choice")

    randomNumber = random.randint(1, 3) #GENRATE THE RANDOM NUMBER BETWEEN 1 - 3 IF NUMBER 1 COMES THAT MEANS STONE , NUMBER 2 COMES THAT MEANS PAPER , NUMBER 3 COMES THAT MEANS SCISSOR 

    if(randomNumber == 1):
        comp = 's'

    elif(randomNumber == 2):
        comp = 'p'

    elif(randomNumber == 3):
        comp = 'sc'

    # TAKE THE INUPUT FROM THE USER 
    userChoice = input(
        "Your's turn : Enter(S) For stone ,Enter (p) for Paper OR Enter (sc) for scissor : ")

    #IF USER SELECTS ANOTHER OPTION WHICH IS NOT IN THE ABOVE OPTIONS THAN SHOW THE ERROR
    if(userChoice != 's' and userChoice != 'p' and userChoice != 'sc'):
        print("\nWarning : You entered invalid Character")

    else:
        print("Computer Selected ==> ", comp)
        print("You Selected  ==> ", userChoice)

        #FUNCTION RETRUN TRUE OR FALSE ACCORIND TO THE DATA GIVEN AND ACCORDING TO THAT THE RESULT GENRATE
        gameResult = gameBegins(comp, userChoice)

        if(gameResult == None):
            print("Sorry Try again , Nobody wins the game")

        elif(gameResult):

            highScore = highScore + 1
            print("Congratualtions , you win the game")

        elif(gameResult == False):
            print("Sorry , Computer Wins the Game")
    numOfTimes = numOfTimes - 1 #DECREMENTING THE COUNTER FOR THE LOOP
    noOfRounds = noOfRounds + 1  #INCREMENTING THE COUNTER FOR SHOWING THE ROUNDS

#FIRST OPEN THE HIGH SCORE TXT FILE AND TAKE THE HIGH SCORE
old_highScore=0
f = open('HighScore.txt','r')
data = f.readlines()
for line in data :
    for c in line:
        if c.isdigit() == True:
            old_highScore = c
f.close()

#AND IF THE HIGH SCORE IS LESS THAN CURRENT SCORE THAN REPLACE THE HIGH SCORE WITH THE CURRENT SCORE
old_highScore = int(old_highScore)
if(highScore > old_highScore):
    f = open('HighScore.txt','w')
    highScore = str(highScore)
    highScore = "High-score : " + highScore
    f.write(highScore)
f.close()
print("\n\n")

#PRINT THE HIGHT SCORE IN THE TERMINAL
f = open('HighScore.txt' , 'r')
print("Current " , f.read())
f.close