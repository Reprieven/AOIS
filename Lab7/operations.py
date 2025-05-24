
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