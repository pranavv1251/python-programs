def depth(eqn):

    list1 = []
    depth = []

    for i in range(0, len(eqn)):
        if eqn[i] == '(':
            list1.append(eqn[i])
            depth.append(len(list1))
        elif eqn[i] == ')':
            list1.pop()
