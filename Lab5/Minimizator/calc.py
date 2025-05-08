from parser_sdnf import parse_sdnf
def count_matches(first: str, second: str)->int:
    if len(first) == len(second):
        matches = len(first)
        for i in range(len(first)):
            if first[i] != second[i] and first.lower() == second.lower():
                matches-=1
        return matches
    else:
        return -1

def adhesion(first: str, second: str)->str:
    repeated_chars = []
    for i in range(len(first)):
        if first[i] == second[i]:
            repeated_chars.append(first[i])
    return ''.join(repeated_chars)

def delete_adhesioned(result: dict):
    filtered = {}
    for key, value in result.items():
        if value == 0:
            filtered[key] = value
    return filtered
        
def calc_iteration(parsed: dict)-> dict:
    result = parsed.copy()
    elems = list(result.keys())
    all_ads = 0
    for i in range(len(elems)-1):
        matches_needed = len(elems[i])-1
        for j in range(i+1,len(elems)):
            if count_matches(elems[i],elems[j]) == matches_needed:
                adhessed_elem = adhesion(elems[i],elems[j])
                if adhessed_elem not in list(result.keys()):
                    result[adhessed_elem] = 0 
                all_ads += 1
                result[elems[i]] += 1
                result[elems[j]] +=1
    result = delete_adhesioned(result)
    return result, all_ads

def calc_SDNF(expression: str):
    parsed = parse_sdnf(expression)
    iterations = [parsed]
    result, all_ads = calc_iteration(parsed)
    iterations.append(result)
    while True:
        result, all_ads = calc_iteration(result)
        if all_ads:
            iterations.append(result)
        else: 
            break
    return iterations