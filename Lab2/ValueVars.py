from Parse import parser
from SumBinary import sum_binary
def all_vars(expression: str)->dict:
    variables = []
    digits = 0
    for element in expression:
        if element.isalpha() and element not in variables:
            variables.append(element)
    digits = len(variables)
    one = [0]*(digits-1)+[1]
    version = [0]*digits
    truth_dict = {var: [] for var in variables}
    for i in range(2**digits):
        for i in range(len(variables)):
            truth_dict[variables[i]].append(version[i])
        version = sum_binary(version,one,digits)
    return truth_dict
        


