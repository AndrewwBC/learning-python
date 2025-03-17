# Tuples are immutables

tupleOne = (1, 2, 3, 4, 5)
tupleTwo = 6, 7, 8, 9, 10

tupleOneElement = (5,)

tupleThree = (tupleOne, tupleTwo)

print(tupleThree)

# elements

print(tupleThree[1])

# (a,b) = tupleThree
# print(b)

def funcTuple():
    return tupleOne

a, b, c, d, e = funcTuple()
print(a, b ,c)