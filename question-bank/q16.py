def lists(l):
    l1 = []
    l2 = []
    for i in range(len(l)):
        if l[i][0] == 'x':
            l1.append(l[i])
        else:
            l2.append(l[i])
    l1.append(sorted(l2))
    return l1


print(lists(['xanx', 'port', 'apple', 'wine', 'xampp']))
