# write
file = open('file.txt', 'w')
file.write("Hello, World")
file.close()

#read
with open('file.txt', 'r') as f:
    print(f.read())


# writelines

with open('list.txt', 'w') as listTxt:
    items = ["cup ", "mug ", "hat \n", "TV ", "radio "]
    listTxt.writelines(items)

# readline and readlines

with open("list.txt", "r") as listTxt:
    print(listTxt.readline())
    print(listTxt.readlines())

# while

with open("queen.txt", "r") as queenTxt:
    while True:
        line = queenTxt.readline()
        if(line == ''):
            break
        print(line, queenTxt.tell())