def find_trigger_conditions(bits):
    a = bits["a"]
    b = bits["b"]
    c = bits["c"]

    a_change_condition = "V = 1"

    b_change_condition = None
    for i in range(len(a) - 1):
        if b[i] != b[i + 1]:
            b_change_condition = a[i]
            break

    c_change_condition = None
    for i in range(len(a) - 1):
        if c[i] != c[i + 1]:  
            c_change_condition = (a[i], b[i])
            break
    
    return {
        "a": f"{a_change_condition}",
        "b": f"V = 1, a = {b_change_condition}",
        "c": f"V = 1, a = {c_change_condition[0]}, b = {c_change_condition[1]}"
    }
