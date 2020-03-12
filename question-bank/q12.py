def perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if(s == n):
        return 'perfect'
    else:
        return 'not perfect'


print(perfect(6))
