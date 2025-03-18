from typing import List

def separate_terms_sdnf(expression: str)->List[str]:
    result = []
    open_index = -1
    close_index = -1
    for i in range(len(expression)):
        if expression[i] == "(":
            open_index = i
        elif expression[i] == ")":   
            close_index = i
        if close_index != -1 and open_index != -1:
            result.append(expression[open_index+1:close_index])
            open_index = -1
            close_index = -1
    return result

def change_inversion(terms: List[str])->List[str]:
    terms_no_inversion = []
    for elem in terms:
        modified_elem = ''
        inverse = False
        
        for i in range(len(elem)):
            if elem[i] == "¬":
                inverse = True
            elif inverse:
                modified_elem += elem[i].upper()
                inverse = False
            else:
                modified_elem += elem[i]
        terms_no_inversion.append(modified_elem)
    
    return terms_no_inversion


def parse_sdnf(expression: str)->List[str]:
    parsed = {}
    separated = separate_terms_sdnf(expression)
    changed = change_inversion(separated)
    for elem in changed: 
        parsed[elem] = 0
    return parsed

