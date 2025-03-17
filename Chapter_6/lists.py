import copy

listOfFruits: list = ["Apple", "Banana", "Pineapple"]

# get the list length
#print(len(listOfFruits))

# unpacking

[a, b, c] = listOfFruits
#print(a, b, c)

def func():
    return listOfFruits

x, y, z = func()

#print(x, y, z)

# slices : is just like range function, the
# stop parameter will not be used to show
# the element witch index is equal to the 
#stop value - stop (exclusive)

#print(listOfFruits[0:len(listOfFruits)])


## concat lists

listOne: list = [1,2,3]
listTwo: list = [4,5,6]

listThree = 1 * listOne + 4 * listTwo

#print(listThree)

# Copying lists
# Assigning a list to another variable does not
# create a new list. This means that both lists
# will be changed when one is changed

copyOfList = listThree
#print(id(copyOfList), id(listThree))

# Shallow Copy copies the memory address, 
# but only the superficial elements
# This means that it's possible to make
# references to children nodes of the first node, thinking of a tree
# but it will not appear in the copy, only in the original
print(listThree.copy())
print(listThree[:])

# DeepCopy will not maintain the address memory
# It will generate another object with all the
# elements of the original object, but in a diferent
# memory space
print(copy.deepcopy(listOfFruits))

# removing elements

print(listOfFruits)
del listOfFruits[0]
print(listOfFruits)

# searching a value

if("Banana" in listOfFruits):
    print("It is inside")
else:
    print("It's not")

# list methods

listOfFruits.sort()
listOfFruits.append("Cocoa")
listOfFruits.insert(0, "Coffee")
listOfFruits.remove("Cocoa")
lastElement = listOfFruits.pop()
listOfFruits.reverse()

print(listOfFruits)

# nested lists

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(nested)):
    for j in range(len(nested)):
        print(nested[i][j])

# list comprehension

values = [1, 2, 3, 4, 5, 6]

double = [value * 2 for value in values if value > 2]
print(double)


