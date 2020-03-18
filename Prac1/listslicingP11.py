print("Enter two numbers:")
a = input()
temp = a.split()
a = int(temp[0])
b = int(temp[1])
list1 = list(range(1, 51))
print("slicing: ", list1[a:b])
print("enter a number:")
a = int(input())
count = 0
for i in list1:
    if(a % i == 0):
        count += 1
print("Count:", count)
