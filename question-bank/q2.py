def valley(l):
    a = int(len(l)/2)+1
    l1 = l[0:a]
    l2 = l[len(l):a-2:-1]
    if l1 == l2:
        return True
    else:
        return False


print(valley([4, 3, 2, 1, 2, 3, 4]))
print(valley([3, 2, 1]))
