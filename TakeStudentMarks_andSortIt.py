#take input of marks from the student
student1 = input("Enter your marks : ")
student2 = input("Enter your marks : ")
student3 = input("Enter your marks : ")
student4 = input("Enter your marks : ")
student5 = input("Enter your marks : ")
student6 = input("Enter your marks : ")

#make list of marks of the students
studentMarks=[student1 , student2 , student3 , student4 , student5 , student6]

print(studentMarks)

#sorting the marks of students
studentMarks.sort()
print("The sorted marks ==> ",studentMarks)