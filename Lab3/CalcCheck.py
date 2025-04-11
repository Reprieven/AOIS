from lab2.ValueFinder import solve_expression
from typing import List
from itertools import combinations
def make_str_sdnf(iteraction: dict)->str:
    terms = []
    for key in iteraction.keys():
        term = []
        for char in key:
            if char.isupper(): 
                term.append(f"!{char.lower()}")
            else:  
                term.append(char)
        terms.append(f"({'&'.join(term)})")

    return "|".join(terms)  

def delete_unnecessary_sdnf(iteration: dict) -> dict:
    truth_table = solve_expression(make_str_sdnf(iteration))
    keys = list(iteration.keys())
    minimal_result = iteration.copy()
    for r in range(len(keys), 0, -1):
        for subset in combinations(keys, r):
            temp_result = {key: iteration[key] for key in subset}
            temp_truth_table = solve_expression(make_str_sdnf(temp_result))

            if temp_truth_table == truth_table:
                minimal_result = temp_result
                break

    return minimal_result

def make_str_sknf(iteraction: dict)->str:
    terms = []
    for key in iteraction.keys():
        term = []
        for char in key:
            if char.isupper(): 
                term.append(f"!{char.lower()}")
            else:  
                term.append(char)
        terms.append(f"({'|'.join(term)})")

    return "&".join(terms)  

def delete_unnecessary_sknf(iteration: dict) -> dict:
    truth_table = solve_expression(make_str_sknf(iteration))
    keys = list(iteration.keys())
    minimal_result = iteration.copy()
    for r in range(len(keys), 0, -1):
        for subset in combinations(keys, r):
            temp_result = {key: iteration[key] for key in subset}
            temp_truth_table = solve_expression(make_str_sknf(temp_result))

            if temp_truth_table == truth_table:
                minimal_result = temp_result
                break

    return minimal_result





