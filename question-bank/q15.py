def strings(s):
    c = 0
    l = s.split()
    for i in range(len(l)):
        if len(l[i]) > 2 and l[i][0] == l[i][-1]:
            c += 1
    return c


print(strings('this tot myum ooooopopopoo'))
