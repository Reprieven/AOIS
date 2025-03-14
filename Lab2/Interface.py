from ValueFinder import solve_expression
from SOP import *
from POS import *
from BinToDecimal import bin_to_decimal
def interface(expression: str):
    solved = solve_expression(expression)
    max_key_length = max(len(key) for key in solved.keys())
    header = " | ".join(solved.keys())
    print(header)
    for i in range(len(solved['a'])):  
        row = [str(solved[key][i]) for key in solved]
        print(" | ".join(row))
    print("СДНФ: "+ make_sdnf(solved))
    print("СКНФ: "+ make_sknf(solved))
    print("Числовые формы:")
    print(make_numerical_sdnf(solved))
    print(make_numerical_sknf(solved))
    print("Индексная форма:")
    print(bin_to_decimal(solved["res"]))
    print(solved["res"])
        