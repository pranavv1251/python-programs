def perfect(a):
    sum = 0
    i = 1
    while(i < a):
        if(a % i == 0):
            sum += i
        i += 1
    if(sum == a):
        return 1
    else:
        return 0


a = int(input())
c = perfect(a)
if(c):
    print("true")
else:
    print("False")
