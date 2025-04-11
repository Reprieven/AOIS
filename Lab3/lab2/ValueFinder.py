from lab2.ValueVars import all_vars
from lab2.Parse import parser
from lab2.Operations import *
from typing import List
def max_precedence(expr):
    max = -1
    for element in expr:
        if isinstance(element,str) and max<precedence(element):
            max = precedence(element)
    return max

def apply_operator(op: str, first: int, second: int) -> int:
    if op == '&':
        return conjunction(first,second)
    elif op == '|':
        return disjunction(first,second)
    elif op == '>': 
        return implication(first,second)
    elif op == '~':  
        return equivalence(first,second)

def find_value(expr) -> int:
    i = 0
    while i < len(expr):
        if expr[i] == '!':
            expr[i + 1] = inversion(expr[i + 1])
            expr.pop(i)
        else:
            i += 1

    while len(expr) > 1:
        max_prec = max_precedence(expr)
        for i in range(len(expr)):
            if isinstance(expr[i], str) and precedence(expr[i]) == max_prec:
                first = expr[i - 1]
                op = expr[i]
                second = expr[i + 1]
                result = apply_operator(op, first, second)
                expr[i - 1:i + 2] = [result]
                break
    return expr[0] if expr else 0

def change_to_int(exp_parsed: List[str], truth_table: dict,iteration: int):
    exp_int_parsed = exp_parsed.copy()
    for index, elem in enumerate(exp_int_parsed):
        if elem.isalpha():
            exp_int_parsed[index] = truth_table[elem][iteration]
    return exp_int_parsed

def process_brackets(exp_int_parsed):
    open_index = -1
    close_index = -1
    while True:
        open_index = -1
        close_index = -1
        for j in range(len(exp_int_parsed)):
            if exp_int_parsed[j] == '(':
                open_index = j
            elif exp_int_parsed[j] == ')':
                close_index = j
                break 
        if open_index == -1 or close_index == -1:
            break
        sub_expression = find_value(exp_int_parsed[open_index + 1:close_index])
        exp_int_parsed[open_index:close_index + 1] = [sub_expression]
    return exp_int_parsed

def solve_for_row(exp_parsed, truth_table, i):
        exp_int_parsed = change_to_int(exp_parsed, truth_table, i)
        exp_int_parsed = process_brackets(exp_int_parsed)
        return find_value(exp_int_parsed)

def solve_expression(expression: str)->int:
    exp_parsed = parser(expression)
    truth_table = all_vars(expression)
    truth_table["res"] = []
    for i in range(len(next(iter(truth_table.values())))):
        result = solve_for_row(exp_parsed, truth_table, i)
        truth_table["res"].append(result)
    return truth_table

