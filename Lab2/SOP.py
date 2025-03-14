def make_sdnf(truth_table: dict) -> str:
    terms = []
    variables = truth_table.keys()

    for i in range(len(truth_table['res'])):
        if truth_table['res'][i] == 1:
            term = [
                (var if truth_table[var][i] == 1 else f'¬{var}')
                for var in variables if var != 'res'
            ]
            terms.append('(' + ' ∧ '.join(term) + ')')

    return ' ∨ '.join(terms)

def make_numerical_sdnf(truth_table: dict)->str:
    result = []
    for i in range(len(truth_table['res'])):
        if truth_table['res'][i] == 1:
            result.append(str(i))
    return '('+", ".join(result)+')∨'