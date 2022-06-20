#INTIALIZING THE CLASS 
class Dog:

    #THIS ARE THE CLASS LEVEL OBJECT WHICH WILL GOING TO SAME FOR ALL THE OBJECT WE CREATED
    dog_breed = "Indian/Local"
    typeOfAnimal = "Mammal"

    #INTIALIZING THE METHOD
    def dogInfo(self):
        print("The Type ," , self.typeOfAnimal)
        print("The dog Breed ," , self.dog_breed)


vatsal = Dog() #OBJECT INTIATION 

print(vatsal.dog_breed) #PRINT THE ATTRIBUTE BY USING THE OBJECT
vatsal.dogInfo() #CALLING CLASS METHOD