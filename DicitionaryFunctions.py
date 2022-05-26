#this is dictionary
myDict = {
    "firstName" : "Mahir",
    "middleName" : "Narendrabhai",
    "lastName" : "Patel",
    "marks" : [1,2,3,4,5,6,7,8,9],
    "tuples" : (1,2,3,4,5),
    "quote" : "Just for fun",

    #nested dictionary
    "anotherDict" : {"fathersName" : "Naredrabhai",
                     "father'sMiddlename" : "Narottambhai",
                     "fatherOccupation" : "Business-Man"
                    }

} 

#This is the way to print the values of nested dictionary
print(myDict['anotherDict']["fatherOccupation"])

#this is the way to print the values of the dictionary
print(myDict["firstName"])

#you can change the values of dictionary
myDict["marks"] = [10,20,50]
print(myDict["marks"])

print(myDict.keys())  #print the keys of the dictionary

print(myDict.items())  #print all items of the dictionary with the key ad the values

print(myDict.values()) #print the values of the dictionary

#update the exisiting dictionary by adding new ky values pair in the new dictionary
updateDict = {
    "mahir" : "my name",
    "occupation"  : "student"
}

myDict.update(updateDict)
print(myDict)

print(myDict.get("firstName"))  #get function get the value of the key given by the user