class StudentInfo:

    #THIS IS THE CONSTRUCTOR WHICH IS USED WHEN WE NEED TO PASS THE PARAMETER WHILE ACESSING THE CLASS
    def __init__(self,givenName ,givenSurname, givenAge ):
        self.studentName = givenName  #THIS WILL STORE THE NAME 
        self.studentSurname = givenSurname #THIS WILL STORE THE SURNAME
        self.studentAge = givenAge #THIS WILL STORE THE AGE

    def fullNameOfStudent(self):
        print("The Full name of the student : " , self.studentName,self.studentSurname)

s1 = StudentInfo("Vatsal", "Prajapati" , 19)

print("THE AGE : ",s1.studentAge)
s1.fullNameOfStudent()
        