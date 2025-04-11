import Calc 
import CalcCheck
def conjunction(first: int, second: int)->int:
    return first*second

def disjunction(first: int, second: int)->int:
    return first+second if first+second!=2 else 1

def inversion(first: int)->int:
    return 0 if first else 1

def implication(first: int, second: int)->int:
    return 0 if first == 1 and second == 0 else 1

def equivalence(first: int, second: int)->int:
    return 1 if first == second else 0

def precedence(operation: str):
    precedence = {
    '!': 3,  
    '&': 2,
    '|': 1,
    '>': 0,
    '~': 0
    }
    return precedence.get(operation,-1)

def sdnf_maker(expression: str)->str:
    sdnf = Calc.calc_SDNF(expression)
    sdnf[-1] = CalcCheck.delete_unnecessary_sdnf(sdnf[-1])
    result = []
    for i in range(len(sdnf)):
        keys = list(sdnf[i].keys())
        group = "∨".join(f"({key})" for key in keys)
        result.append(group)
    
    return "\n".join(result)

def sknf_maker(expression: str)->str:
    sknf = Calc.calc_SKNF(expression)
    sknf[-1]= CalcCheck.delete_unnecessary_sknf(sknf[-1])
    result = []
    for dictionary in sknf :
        keys = dictionary.keys()
        group = "".join(f"({key})" for key in keys)
        result.append(group)
    
    return "\n".join(result)

def add_disjunction(iteration: str) -> str:
    result = []
    for i in range(len(iteration) - 1):
        result.append(iteration[i])
        if iteration[i].isalpha() and iteration[i + 1] != ")":
            result.append("v")
    result.append(iteration[-1])
    return ''.join(result)  

def replace(iterations: str)->str:
    result = ""
    for elem in iterations:
        if elem.isupper():
            result+=f"¬{elem.lower()}"
        else :
            result+=elem
    return result       
    
def sdnf_karno(expression: str, implicants)->str:
    dnf = sdnf_maker(expression)
    dnf = replace(dnf)
    return dnf.splitlines()[-1]

def sknf_karno(expression: str, implicants)->str:
    knf = sknf_maker(expression)
    knf = add_disjunction(knf)
    knf = replace(knf)
    return knf.splitlines()[-1]