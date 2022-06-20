class Counter:

    def __init__(self):
        self.__counter  = 0

    def increment(self):
        self.__counter += 1
    
    def counterValue(self):
        return self.__counter

    def resetCounter(self):
        self.__counter =0

#DUE TO BELOW PROBLEM WE NEED THE PRIVATE ATTRIBUTES BECAUSE YOU CAN SEE ANYONE CAN CHANGE THE VALUE OF COUNTER FROM THE OUTSIDE OF THE CLASS

#BY USINNG THE DOUBLE UNDERSCORE THE PYTHON KNOWS THAT IT IS PRIVATE ATTRIBUTE AND IT CANNOT BE CHANGE FROM OUTSIDE OF THE CLASS

obj1 = Counter()

obj1.increment()
obj1.increment()
obj1.increment()

print("The value of the counter : ",obj1.counterValue())

obj1.__counter = 999  

print(f"The value after changing the value of the counter : {obj1.counterValue()}")

