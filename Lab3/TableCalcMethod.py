from CalcMethod import calc_SDNF, calc_SKNF
from typing import List
def contains_substring(main_string, substring):
    return substring in main_string

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
        
def remove_by_value(input_dict, value_to_remove):
    keys_to_remove = []

    for key, value in input_dict.items():
        if value == value_to_remove:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        del input_dict[key]

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

def table_calc_sdnf(expression: str):
    table = form_table_sdnf(expression)
    keys = list(table.keys()) 

    for i in range(len(keys) - 1):
        for j in range(i + 1, len(keys)):
            value_i = table.get(keys[i])
            value_j = table.get(keys[j])
            
            if value_i is not None and value_j is not None:
                sub_array = arrays_contain(value_i, value_j)
            if sub_array:
                remove_by_value(table, sub_array)

    return table

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
    keys = list(table.keys()) 

    for i in range(len(keys) - 1):
        for j in range(i + 1, len(keys)):
            sub_array = arrays_contain(table[keys[i]], table[keys[j]])
            if sub_array:
                remove_by_value(table, sub_array)

    return table

    