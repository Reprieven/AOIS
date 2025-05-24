from matrix_maker import *

def find_word(matrix, index):
    if index >= len(matrix):
        return None
    else:
        matrix_col = make_matrix_col(matrix)
        col = matrix_col[index]
        if index == 0:
            return col
        end = col[:index]
        start = col[index:]
        word = start+end
        return word
        
def find_address_col(matrix, index):
    if index >= len(matrix):
        return None
    address_col = []
    i = index
    j = 0
    while True:
        address_col.append(matrix[i][j])
        i+=1
        j+=1
        if i >=len(matrix):
            i = 0
        if j>=len(matrix):
            break
    return address_col
