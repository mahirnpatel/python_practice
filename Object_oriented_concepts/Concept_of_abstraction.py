#WE HAVE TO IMPOR THE ABC FROM ABC AND ALSO IMPOR ABSTRACTMETHOD
from abc import ABC,abstractmethod

# WHAT IS ABSTRACTION OR WHAT IS ABSTRACTION CLASS
# ==> ABSTRACTION CLASS IS CLASS IN WHICH ALL OTHER CLASS WHICH IS INHERITED FROM THE ABSTRACTION CLASS SHOULD ALSO HAVE THE SAME METHOD LIKE ABSTRACT METHOD

#ABSTRACT CLASS OF CAR
class Car(ABC):
    @abstractmethod
    def milege(self):
        pass

class tesla(Car):

    def milege(self):
        print("THe milege of the telsa car : 30km/h")

class toyota(Car):

    def milege(self):
        print("THe milege of the Toyata car : 60km/h")

class Mahindra(Car):

    def milege(self):
        print("THe milege of the Mahindra car : 20km/h")

class Maruti(Car):

    def Car_engine(self):
        print("THe car engine of the Maruti car : Very bad")

t = tesla()
t.milege()

#THIS THROWS THE ERROR AS IT INHERITATE THE CAR CLASS AND AS PER THAT IT IS ABSTRACT CLASS SO THE MARUTI CLASS HAVE COMPULSORY CONTAIN THE MILEGE FUNCTION/METHOD
obj1 = Maruti()
obj1.Car_engine()

