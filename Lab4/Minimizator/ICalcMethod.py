from Calc import calc_SDNF
def separate_iterations_sdnf(expression: str)->str:
    sdnf = calc_SDNF(expression)
    result = []
    for i in range(len(sdnf)):
        keys = list(sdnf[i].keys())
        group = "∨".join(f"({key})" for key in keys)
        result.append(group)
    
    return "\n".join(result)

def replace_upper_case_with_inversion(iterations: str)->str:
    result = ""
    for elem in iterations:
        if elem.isupper():
            result+=f"¬{elem.lower()}"
        else :
            result+=elem
    return result       
    
def sdnf_interface_calc(expression: str)->str:
    print("Расчетный метод")
    print("Итерации СДНФ")
    Isdnf = separate_iterations_sdnf(expression)
    Isdnf = replace_upper_case_with_inversion(Isdnf)
    print(Isdnf)
