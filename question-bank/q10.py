def strings(s):
    c = 0
    d = 0
    for i in range(len(s)):
        if s[i].isupper():
            c += 1
        else:
            d += 1
    print(c, d)


print(strings('JijU'))
