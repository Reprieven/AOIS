from typing import List
from matrix_maker import make_matrix_col
from find_by_index import find_word

def compare_words(first_word:List[int], second_word:List[int]):
    for i in range(len(first_word)):
        if first_word[i] > second_word[i]:
            return False
        elif first_word[i] < second_word[i]:
            return True
    return False

def sort(matrix: List[int]):
    matrix_col = make_matrix_col(matrix)
    words_list = []
    for i in range(len(matrix_col)):
        words_list.append(find_word(matrix,i))
    for i in range(len(words_list)-1):
        for j in range(i,len(words_list)):
            max_word = words_list[i]
            if compare_words(words_list[i], words_list[j]):
                max_word = words_list[j]
                words_list[j] = words_list[i]
                words_list[i] = max_word
                buf = matrix_col[j]
                matrix_col[j] = matrix_col[i]
                matrix_col[i] = buf
    return make_matrix_col(matrix_col)