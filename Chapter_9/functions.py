def sum(a, b):
     return a + b

result = sum(12, 12)

# print(result)

# default value

def multiply(a, b = 5):
     return a * b

result1 = multiply(2)

# print(result1)

# global variable

def funcao():
     global x 
     x = 20
     print(x)

x = 10
funcao()
print(x)