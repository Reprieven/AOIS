from find_by_index import find_word
from sum_binary import sum_binary
from matrix_maker import make_matrix_col
from typing import List

def find_sum(matrix: List[List[int]],v: List[int]):
    matrix_col = make_matrix_col(matrix)
    words_list = []
    for i in range(len(matrix)):
        words_list.append(find_word(matrix, i))
    words_num = len(words_list)
    a_len = 4
    b_len = 4
    for i in range(words_num):
        word = words_list[i]
        if word[:len(v)] == v:
            A = word[len(v):len(v)+a_len]
            B = word[len(v)+a_len:len(v)+a_len+b_len]
            sum_A_B = sum_binary(A, B)
            result_word = v+A+B+sum_A_B
            matrix_col[i] = result_word
    return make_matrix_col(matrix_col)
    