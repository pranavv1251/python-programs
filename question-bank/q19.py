def strings(s):
    c = s[0]
    s1 = s[0]
    for i in range(1, len(s)):
        if s[i] == c:
            s1 += '*'
        else:
            s1 += s[i]
    return s1


print(strings('anatas'))
