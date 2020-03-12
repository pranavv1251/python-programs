def sublist(l1, l2):
    for i in range(0, len(l1)):
        if l1[i] == l2[0]:
            f = 0
            for j in range(0, len(l2)):
                if l1[i+j] != l2[j]:
                    f = 1
                    break
    if f == 0:
        return True
    else:
        return False


print(sublist([1, 2, 3, 4], [1,  3]))
