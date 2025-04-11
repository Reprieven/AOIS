def make_sknf(truth_table: dict) -> str:
    terms = []
    variables = truth_table.keys()

    for i in range(len(truth_table['res'])):
        if truth_table['res'][i] == 0:
            term = [
                (f'¬{var}' if truth_table[var][i] == 1 else var)
                for var in variables if var != 'res'
            ]
            terms.append('(' + ' ∨ '.join(term) + ')') 

    return ' ∧ '.join(terms)
