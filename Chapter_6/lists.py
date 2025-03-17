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










