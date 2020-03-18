list1 = []
largest = ''
line = input("Enter words:")
while(line != ''):
    if(len(largest) <= len(line)):
        largest = line
    line = input()
print(f'The largest word is {largest} and its length is {len(largest)}')
