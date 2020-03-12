
def one_hop(l):
    f = []
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            print(l[0][1])
            if l[i][1] == l[j][0] and l[i][0] != l[j][1]:
                f += [(l[i][0], l[j][1])]
    myset = set(f)
    return (sorted(myset))


print(one_hop([(2, 3), (1, 2)]))
print(one_hop([(2, 3), (3, 4)]))
