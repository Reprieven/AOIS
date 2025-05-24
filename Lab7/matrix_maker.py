import random

def make_matrix(size: int):
    matrix = []
    for i in range(size):
        matrix.append([0]*size)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(0,1)
    return matrix

def make_matrix_col(matrix):
    result = []
    for i in range(len(matrix)):
        col = []
        for j in range(len(matrix)):
            col.append(matrix[j][i])
        result.append(col)
    return result