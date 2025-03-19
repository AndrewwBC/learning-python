# text = "Python"

# text = 'Python'

# text = '''P
# y
# t
# h
# o
# n'''

# print(text)

# elements

name = "Andrew"

# Strings are immutable

#name[0] = "N"

for i in range(len(name)):
    print(name[i])


car = "Chevrolet"

print(car[:4], car[4:], car[0:9:2])

# string formatting

oldValue = 4
newValue = 5.25

info = "Old value is %d and the new value is %.2f" % (oldValue, newValue)
print(info)

# raw and normal string

print("Normal string")
print(r"Raw string")

# string inside another string

str1 = "Python is a programming language"
str2 = "Python"

if str2 in str1: 
    print("Found")
else:
    print("Not found")
