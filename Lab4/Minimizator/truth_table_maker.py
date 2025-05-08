from itertools import product

def generate_d():
    inputs = list(product([0, 1], repeat=3))
    table = {"a": [], "b": [], "c": [], "res": []}
    
    for a, b, c in inputs:
        d = a ^ b ^ c 
        table["a"].append(a)
        table["b"].append(b)
        table["c"].append(c)
        table["res"].append(int(d))
    
    return table

def generate_bi():
    inputs = list(product([0, 1], repeat=3))
    table = {"a": [], "b": [], "c": [], "res": []}
    
    for a, b, c in inputs:
        bi = (not a and b) or (not a and c) or (b and c)
        table["a"].append(a)
        table["b"].append(b)
        table["c"].append(c)
        table["res"].append(int(bi))
    
    return table

def generate_plus_2_table():
    table = {
        "W": [], "X": [], "Y": [], "Z": [],
        "W'": [], "X'": [], "Y'": [], "Z'": []  
    }
    
    for num in range(16):
        W, X, Y, Z = (num >> 3) & 1, (num >> 2) & 1, (num >> 1) & 1, num & 1
        
        table["W"].append(W)
        table["X"].append(X)
        table["Y"].append(Y)
        table["Z"].append(Z)
        
        if num <= 9:
            plus2 = num + 2
            W_p, X_p, Y_p, Z_p = (plus2 >> 3) & 1, (plus2 >> 2) & 1, (plus2 >> 1) & 1, plus2 & 1
        else: 
            W_p = X_p = Y_p = Z_p = None
        
        table["W'"].append(W_p)
        table["X'"].append(X_p)
        table["Y'"].append(Y_p)
        table["Z'"].append(Z_p)
    
    return table



