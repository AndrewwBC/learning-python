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

print(listThree)











