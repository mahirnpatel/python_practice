
name=["mahir" , "swara" , "vatsal" , "kavish" , 200 , 20.20 , False , True]

print(name) #print the list 

print("The length of the this list ==> " , len(name)) #print the length of list

print(name[0])  #accessing the index of the list 

name[4] = 4000  #changing the value of index 4 
print(name[4])  

print("The elements in the list from 0 index to the 4 index",name[0:5]) #this is the slicing of the list 

numList=[20,4,5,6,7,1,2,3] # list contaning numbers
print(numList)

numList.sort()  #sorting the list 
print(numList)

numList.reverse() #reverse the list i.e from the last index to the first index
print(numList)

numList.append("mahir")  #add the new string or number or float to the end of the list i.e last index
print(numList)

numList.insert(2,False) #add the given data to the particular given index
print(numList)

x=numList.pop(2) #delete the data present at the index 2 and you can also store the value in the variable
print(x)
print(numList)

numList.remove("mahir")  #delete the passed data from the list 
print(numList)

#this is the example of the reverse function 
name=["mahir","swara" , "vatsal" , "kavish","manav" , "neer" , "datt"]
name.reverse()
print(name)
