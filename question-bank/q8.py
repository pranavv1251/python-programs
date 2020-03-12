def secondmax(l):
    c = 0
    d = l[0]
    for i in l:
        if c <= i:
            c = i
    print(c)
    for j in l:
        if d <= j and j != c:
            d = j
    return d


print(secondmax([1, 2, 3, 4]))
