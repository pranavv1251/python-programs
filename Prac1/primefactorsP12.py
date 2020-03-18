print('Enter number:')
a = int(input())
i = 1
while (i < a):
    if(a % i == 0):
        print("Factor: ", i)
        flag = 0
        j = 2
        while j < i:
            if(i % j == 0):
                print("Not Prime")
                flag = 1
                break
            j += 1
        if(flag == 0):
            print("Prime number")
    i += 1
