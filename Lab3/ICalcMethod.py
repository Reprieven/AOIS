from CalcMethod import calc_SDNF, calc_SKNF

def separate_iterations_sdnf(expression: str)->str:
    sdnf = calc_SDNF(expression)
    result = []
    for dictionary in sdnf :
        keys = dictionary.keys()
        group = "∨".join(f"({key})" for key in keys)
        result.append(group)
    
    return "\n".join(result)

def separate_iterations_sknf(expression: str)->str:
    sknf = calc_SKNF(expression)
    result = []
    for dictionary in sknf :
        keys = dictionary.keys()
        group = "".join(f"({key})" for key in keys)
        result.append(group)
    
    return ";\n".join(result)

def add_disjunction(iteration: str) -> str:
    result = []
    for i in range(len(iteration) - 1):
        result.append(iteration[i])
        if iteration[i].isalpha() and iteration[i + 1] != ")":
            result.append("v")
    result.append(iteration[-1])
    return ''.join(result)  

def replace_upper_case_with_inversion(iterations: str)->str:
    result = ""
    for elem in iterations:
        if elem.isupper():
            result+=f"¬{elem.lower()}"
        else :
            result+=elem
    return result

def sdnf_interface_calc(expression: str)->str:
    Isdnf = separate_iterations_sdnf(expression)
    Isdnf = replace_upper_case_with_inversion(Isdnf)
    print(Isdnf)

def sknf_interface_calc(expression: str)->str:
    Isknf = separate_iterations_sknf(expression)
    Isknf = add_disjunction(Isknf)
    Isknf = replace_upper_case_with_inversion(Isknf)
    print(Isknf)