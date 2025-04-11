from Calc import calc_SDNF, calc_SKNF
from typing import List
def contains_substring(main_string, substring):
    is_substr = 0
    for elem in substring:
        if elem in main_string:
            is_substr+=1
    return is_substr == len(substring)

def x_count(arr1,arr2):
    x_count1 = 0
    x_count2 = 0
    for i in range(len(arr1)):
        if arr1[i] == "X":
            x_count1+=1
        if arr2[i]=="X":
            x_count2+=1
    return x_count1,x_count2

def arrays_contain(arr1, arr2):
    x_count1, x_count2 = x_count(arr1=arr1,arr2=arr2)
    if x_count1>x_count2:
        super_arr = arr1
        sub_arr = arr2 
    else:
        super_arr=arr2
        sub_arr = arr1
    for i in range(len(super_arr)):
        if super_arr[i] == "" and sub_arr[i] == "X":
            return None
    return sub_arr
        
def remove_unnecessary(input_dict, keys_to_keep):
    result = {}
    for key in input_dict.keys():
        if key in keys_to_keep:
            result[key] = input_dict[key]
    return result
    

def form_table_sdnf(expression: str)->dict:
    iterations = calc_SDNF(expression)
    res_elements = iterations[-1]
    constituents = iterations[0]
    columns = len(constituents.keys())
    for key in res_elements.keys():
        res_elements[key] = [""] * columns

    for elem in res_elements.keys():
        index = 0 
        for const in constituents.keys():
            if contains_substring(const, elem):
                res_elements[elem][index] = "X"
            index += 1
    return res_elements

def minimal_set_cover(table: dict):
    all_positions = set()
    for key, value in table.items():
        for i, v in enumerate(value):
            if v == 'X':
                all_positions.add(i)

    cover_map = {key: {i for i, v in enumerate(value) if v == 'X'} for key, value in table.items()}

    selected_sets = []
    uncovered_positions = all_positions.copy()

    while uncovered_positions:
        best_set = None
        best_coverage = set()

        for key, covered_positions in cover_map.items():
            coverage = covered_positions & uncovered_positions 
            if len(coverage) > len(best_coverage):
                best_set = key
                best_coverage = coverage

        selected_sets.append(best_set)
        uncovered_positions -= best_coverage

    return selected_sets

def table_calc_sdnf(expression: str):
    table = form_table_sdnf(expression)
    minimal_elements = minimal_set_cover(table)
    minimize_table = remove_unnecessary(table,minimal_elements)

    return minimize_table

def form_table_sknf(expression: str)->dict:
    iterations = calc_SKNF(expression)
    res_elements = iterations[-1]
    constituents = iterations[0]
    columns = len(constituents.keys())
    for key in res_elements.keys():
        res_elements[key] = [""] * columns

    for elem in res_elements.keys():
        index = 0 
        for const in constituents.keys():
            if contains_substring(const, elem):
                res_elements[elem][index] = "X"
            index += 1
    return res_elements

def table_calc_sknf(expression: str):
    table = form_table_sknf(expression)
    minimal_elements = minimal_set_cover(table)
    minimize_table = remove_unnecessary(table,minimal_elements)
    return minimize_table

    