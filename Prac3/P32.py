ul = []
dl = []
line = input("Enter list")
while(line != ''):
    if line not in ul:
        ul.append(line)
    else:
        dl.append(line)
    line = input()
print('The original list is: ', ul)
print('The duplicate items are: ', dl)
