from datetime import datetime  #import date and time module 
from playsound import playsound # import playsound module

#TAKE THE TIME FROM THE USER 
userTime = input("Enter the time in the : HH:MM:SS (24 HOURS FORMAT)  => ");
print(userTime)

user_Hour = userTime[0:2]  #THIS WILL STORE THE USER'S GIVEN HOUR
user_Minute = userTime[3:5] #THIS WILL STORE THE USER'S GIVEN MINUTE
user_Second = userTime[6:] #THIS WILL STORE THE USER'S GIVEN SECOND

print("Alaram set........")

while(True):
    #STORE THE CURRENT TIME INCLUDING HOURS MINUTE ANE SECOND IN THE VARIABLES
    current_Time = datetime.now()  
    current_Hour = current_Time.strftime("%H")
    current_Minute = current_Time.strftime("%M")
    current_Second = current_Time.strftime("%S")

    #IF MATCH THAN PLAY THE ALARAM OR ELSE DO NOTHING
    if(user_Hour == current_Hour):
        if(user_Minute == current_Minute):
            if(user_Second == current_Second):
                print("Wake up!!")
                playsound("love_alarm.mp3")
                break



    