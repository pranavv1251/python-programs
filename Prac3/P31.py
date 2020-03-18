list_1 = []
sorted = []
line = input("enter tuples:")
while(line != ''):
    list_1.append(tuple(line.split()))
    line = input()
print(list_1)
list_1.sort(key=lambda x: x[-1])
print("Sorted list is ", list_1)
