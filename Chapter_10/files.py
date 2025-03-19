# write
file = open('file.txt', 'w')
file.write("Hello, World")
file.close()

#read
with open('file.txt', 'r') as f:
    print(f.read())
