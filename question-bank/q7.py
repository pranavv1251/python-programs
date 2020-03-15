def transpose(matr):
    result = [[0 for x in range(len(matr))] for y in range(len(matr[0]))]
    print(result)
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            result[j][i] = matr[i][j]

    return result


print(transpose([[1, 4, 9]]))
print(transpose([[1, 3, 5], [2, 4, 6]]))
print(transpose([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
