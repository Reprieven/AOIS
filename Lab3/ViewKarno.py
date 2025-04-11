def generate_gray_code(n):
    if n == 0:
        return ['']
    lower = generate_gray_code(n - 1)
    return ['0' + code for code in lower] + ['1' + code for code in reversed(lower)]

def print_karno_gray(table):
    rows = len(table)
    cols = len(table[0]) if rows > 0 else 0
    
    row_bits = (rows - 1).bit_length() if rows > 1 else 1
    col_bits = (cols - 1).bit_length() if cols > 1 else 1

    row_gray = generate_gray_code(row_bits)[:rows]
    col_gray = generate_gray_code(col_bits)[:cols]

    max_len = max(len(str(cell)) for row in table for cell in row)
    gray_len = max(len(g) for g in row_gray + col_gray)
    cell_width = max(max_len, gray_len)
    
    print(" " * (gray_len + 2) + " ".join(f"{g:^{cell_width}}" for g in col_gray))
    
    print(" " * (gray_len + 1) + "+" + "-" * ((cell_width + 1) * len(col_gray)) + "+")
    
    for i, (gray, row) in enumerate(zip(row_gray, table)):
        print(f"{gray:>{gray_len}} | " + " ".join(f"{cell:^{cell_width}}" for cell in row) + " |")
    
    print(" " * (gray_len + 1) + "+" + "-" * ((cell_width + 1) * len(col_gray)) + "+")
