def ends(s):
    s1 = ''
    s1 += s[0]
    s1 += s[1]
    s1 += s[-2]
    s1 += s[-1]
    return s1


print(ends('spring'))
