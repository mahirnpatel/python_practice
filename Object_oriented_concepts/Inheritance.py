# THIS IS THE BASE CLASS
class Grandparent:
    def Fun1(self):
        print("Granparent class")

    def __init__(self, grandParentname):
        self.name = grandParentname

# THIS IS THE PARENT CLASS WHICH INHERIT THE METHODS OF THE GRANDPARENT CLASS


class Parent(Grandparent):

    def fun2(self):
        print("parent class which inherit the granparent class")

    def __init__(self, grandParentname, parentName):
        super().__init__(grandParentname)
        self.parentname = parentName

# THIS IS THE CHILD CLASS WHICH INHERIT THE METHODS OF THE PARENT AND GRANDPARENT CLASS
class Child(Parent):

    def fun3(self):
        print("Child class which inherits both parent and granparent class ")

    def __init__(self, grandParentname, parentName, childName):

        super().__init__(grandParentname, parentName)
        self.childname = childName


# child1 = Child()  # INTIALIZE THE OBJECT FOR ACCESING THE CLASS

# WE CAN ACCESS THE PROPERTIES OR METHOD OF ANY CLASS BY ACCESSING THE child CLASS AS IT INHERIT THE METHODS OF PARENT ADN GRANDPARENT CLASS
# child1.Fun1()
# child1.fun2()
# child1.fun3()

child2 = Child("Mahir", "Narendrabhai", "Narottambhai")

print(" Grandparent  Name  ==> ", child2.name)
print(" Parent Name  ==> ", child2.parentname)
print(" Child Name  ==> ", child2.childname)
