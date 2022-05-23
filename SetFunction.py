'''IMPORTANT NOTE :- Only the object which is not changable for example tuples is only add in the set

Set have no indexed and you cannot add the same number again in the set 
''' 

#printing the set contaning the values


set1={1,2,3,4}
print(set1)

#if you want to print the empty set than you will make empty set by below syntax:

mySet = set()
print("The type of the set ==> ",type(mySet))

#Diffrent operation of set :

#add function add the values in the set
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)

print(len(mySet))  #retruns the length of the set

mySet.remove(3)  #remove the given element from the set  
print("The updated set ==> " , mySet)

print("The poped element from the set ==> ", mySet.pop()) #it pop out the first element from the set

# mySet.clear()  #it clear the all element from the set
print(mySet)
