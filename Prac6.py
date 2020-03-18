import numpy as np


class MyMatrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = np.random.random((rows, cols))

    def add(self, add_matr):
        self.matrix = np.add(self.matrix, add_matr)
        return self.matrix

    def subt(self, sub_matr):
        self.matrix = np.subtract(self.matrix, sub_matr)
        return self.matrix

    def mult(self, mul_mat):
        self.matrix = np.matmul(self.matrix, mul_mat)
        return self.matrix

    def inverse(self):
        self.matrix = np.linalg.inv(self.matrix)
        return self.matrix


class SqrMatrix(MyMatrix):
    def __init__(self, rows, cols):
        super().__init


mat = MyMatrix(2, 2)
add_mat = [(2, 2),
           (2, 2)]
print('Addition: ', mat.add(add_mat))
print('Subtraction: ', mat.subt(add_mat))
print('Multiplication: ', mat.mult(add_mat))
print('Inverse: ', mat.inverse())
