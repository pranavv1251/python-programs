def maxcount(l):
    freq = 0
    for i in l:
        if freq <= l.count(i):
            freq = l.count(i)
    return freq


print(maxcount([1, 2, 2, 3, 2, 2, 2]))
