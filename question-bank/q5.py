l = input("Enter the input: ")
a = []
while(l != ''):
    a.append(l)
    l = input()
for i in range(int(len(a)/2), len(a)):
    print(a[i])
for i in range(0, int(len(a)/2)):
    print(a[i])
