print("Enter two numbers:")
a = input()
temp = a.split()
a = int(temp[0])
b = int(temp[1])
list2 = []
for i in range(a, b+1):
    square = 0
    for j in range(1, i+1):
        if(j*j == i):
            square = 1
            break
    n = i
    s = 0
    while n != 0:
        rem = int(n % 10)
        s += rem
        n = int(n/10)
        # print(s)
    if(square and s < 10):
        list2.append(i)
print("Number: ", list2)
