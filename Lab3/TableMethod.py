from lab2.ValueFinder import solve_expression
import math
from lab2.Operation import *
from lab2 import POS, SOP
from typing import List, Tuple
from itertools import combinations

def gray_code(num: int) -> int:
    return num ^ (num >> 1)

def gray_code_to_list(num: int, vars_num: int) -> List[int]:
    gray_code_int = gray_code(num)
    result = []
    for i in range(vars_num-1, -1, -1):
        result.append((gray_code_int >> i) & 1)
    return result

def make_karno_table(expression):
    data = solve_expression(expression)
    variables = [var for var in data.keys() if var != 'res']
    num_vars = len(variables)
    
    if num_vars < 2:
        raise ValueError("Нужно как минимум 2 переменные для карты Карно")
    
    rows_vars = variables[:num_vars//2]
    cols_vars = variables[num_vars//2:]
    
    def gray_code(n):
        if n == 0:
            return ['']
        lower = gray_code(n-1)
        return ['0' + code for code in lower] + ['1' + code for code in reversed(lower)]
    
    row_gray = gray_code(len(rows_vars))
    col_gray = gray_code(len(cols_vars))
    
    rows = 2 ** len(rows_vars)
    cols = 2 ** len(cols_vars)
    k_map = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(len(data['res'])):
        values = {var: data[var][i] for var in variables}
        res = data['res'][i]

        row_bits = ''.join(str(values[var]) for var in rows_vars)
        col_bits = ''.join(str(values[var]) for var in cols_vars)
        
        row = row_gray.index(row_bits)
        col = col_gray.index(col_bits)

        k_map[row][col] = res
    
    return k_map

def make_zeros_table_from_karno(karno: List[List[int]]):
    zeros_table = [[0 for _ in range(len(karno[0]))] for _ in range(len(karno))]
    return zeros_table

def count_area(rectangle)->int:
    count = 0
    for elem in rectangle:
        if isinstance(elem, list):
            count+=len(elem)
        else:
            count+=1
    return count

def check_area(rectangle)->bool:
    count = count_area(rectangle)
    log_value = math.log2(count)
    return log_value.is_integer()

def split_columns_with_coordinates(karno):
    result = []
    
    for j, col in enumerate(zip(*karno)):
        i = 0
        while i < len(col):
            if col[i] != 1:
                i += 1
                continue
            
            block_size = 1
            if i + 1 < len(col) and col[i+1] == 1:
                block_size = 2
            
            result.append(([1]*block_size, (i, j)))
            i += block_size
    
    return result

def split_rows_with_coordinates(karno):
    result = []
    
    for i, row in enumerate(karno):
        j = 0
        while j < len(row):
            if row[j] != 1:
                j += 1
                continue
            
            block_size = 1
            if j + 1 < len(row) and row[j+1] == 1:
                block_size = 2
            
            result.append(([1]*block_size, (i, j)))
            j += block_size
    
    return result

def compound_cols_depth(split_cols: List):
    result = split_cols.copy()
    n = len(split_cols)
    for i in range(n-1):
        for j in range(i+1, n):
            new_block = []
            block_i, coord_i = split_cols[i]
            block_j, coord_j = split_cols[j]
            if coord_i[1]==coord_j[1] and coord_i[0]+len(block_i) == coord_j[0]:
                new_block = block_i+block_j
                new_coord = (min(coord_i[0], coord_j[0]), coord_i[1])
            if new_block and check_area(new_block):
                result.append((new_block, new_coord))
    return result

def compound_rows_depth(split_rows: List):
    result = split_rows.copy()
    n = len(split_rows)
    for i in range(n-1):
        for j in range(i+1, n):
            new_block = []
            block_i, coord_i = split_rows[i]
            block_j, coord_j = split_rows[j]
            if coord_i[0]==coord_j[0] and coord_i[1]+len(block_i) == coord_j[1]:
                new_block = block_i+block_j
                new_coord = (min(coord_i[0], coord_j[0]), coord_i[1])
            if new_block and check_area(new_block):
                result.append((new_block, new_coord))
    return result       

def compound_cols_width(split_cols: List):
    result = []
    n = len(split_cols)
    used = set()
    for i in range(n-1):
        for j in range(i+1, n):
            new_block = []
            block_i, coord_i = split_cols[i]
            block_j, coord_j = split_cols[j]
            if len(block_i) != len(block_j):
                continue
            if coord_i[0]!= coord_j[0]:
                continue
            if abs(coord_i[1]-coord_j[1])!=1:
                continue
            new_block = [block_i, block_j]
            if check_area(new_block):
                used.add(tuple(block_i))
                used.add(tuple(block_j))
                new_coord = (coord_i[0], min(coord_i[1], coord_j[1]))
                result.append((new_block,new_coord))

    for i in range(n):
        if tuple(split_cols[i][0]) not in used:
            result.append(split_cols[i])

    return result

def compound_rows_width(split_rows: List):
    result = []
    n = len(split_rows)
    used = set()
    for i in range(n-1):
        for j in range(i+1, n):
            new_block = []
            block_i, coord_i = split_rows[i]
            block_j, coord_j = split_rows[j]
            if len(block_i) != len(block_j):
                continue
            if coord_i[1]!= coord_j[1]:
                continue
            if abs(coord_i[0]-coord_j[0])!=1:
                continue
            new_block = [block_i, block_j]
            if check_area(new_block):
                used.add(tuple(block_i))
                used.add(tuple(block_j))
                new_coord = (min(coord_i[0], coord_j[0]), coord_i[1])
                result.append((new_block,new_coord))

    for i in range(n):
        if tuple(split_rows[i][0]) not in used:
            result.append(split_rows[i])

    return result

def add_column(matrix: List[List[int]], column: Tuple):
    block = column[0]
    coord_i = column[1][0]
    coord_j = column[1][1]
    if isinstance(block[0], int):
        for elem in block:
            matrix[coord_i][coord_j] = elem
            coord_i+=1
    else:
        for col in block:
            for elem in col:
                matrix[coord_i][coord_j] = elem
                coord_i+=1
            coord_i = column[1][0]
            coord_j+=1
    return matrix

def add_row(matrix: List[List[int]], row: Tuple):
    block = row[0]
    coord_i = row[1][0]
    coord_j = row[1][1]
    if isinstance(block[0], int):
        for elem in block:
            matrix[coord_i][coord_j] = elem
            coord_j+=1
    else:
        for line in block:
            for elem in line:
                matrix[coord_i][coord_j] = elem
                coord_j+=1
            coord_j = row[1][1]
            coord_i+=1
    return matrix

def make_table_from_columns(karno: List[List[int]], compounded_columns: List):
    result_matrix = make_zeros_table_from_karno(karno)
    for col in compounded_columns:
        result_matrix = add_column(result_matrix, col)
    return result_matrix

def make_table_from_rows(karno: List[List[int]], compounded_rows: List):
    result_matrix = make_zeros_table_from_karno(karno)
    for row in compounded_rows:
        result_matrix = add_row(result_matrix, row)
    return result_matrix

def make_table_from_columns_and_rows(karno: List[List[int]], compounded_columns: List, compounded_rows: List):
    result_matrix = make_zeros_table_from_karno(karno)
    for col in compounded_columns:
        result_matrix = add_column(result_matrix, col)
    for row in compounded_rows:
        result_matrix = add_row(result_matrix, row)
    return result_matrix

def get_ones_positions(karno):
    return [(i, j) for i, row in enumerate(karno) 
                   for j, val in enumerate(row) if val == 1]

def process_element(element, covered, cols):
    arr, (start_i, start_j) = element
    if isinstance(arr[0], list):
        process_2d_block(arr, start_i, start_j, covered)
    else:
        process_1d_block(arr, start_i, start_j, covered, element in cols)

def process_2d_block(arr, start_i, start_j, covered):
    for di, row in enumerate(arr):
        for dj, val in enumerate(row):
            if val == 1:
                covered.add((start_i + di, start_j + dj))

def process_1d_block(arr, start_i, start_j, covered, is_column):
    for k, val in enumerate(arr):
        if val == 1:
            if is_column:
                covered.add((start_i + k, start_j))
            else:
                covered.add((start_i, start_j + k))

def check_coverage(combo, ones_positions, cols):
    covered = set()
    for element in combo:
        process_element(element, covered, cols)
    return covered.issuperset(ones_positions)

def find_separate_cover(karno, cols, rows):
    ones_positions = get_ones_positions(karno)
    min_cols = None
    min_rows = None
    min_size = float('inf')

    for cols_count, rows_count in generate_size_combinations(cols, rows, min_size):
        current_size = cols_count + rows_count
        found_cols, found_rows = check_separate_combinations(
            cols, rows, cols_count, rows_count, ones_positions)
        
        if found_cols is not None and current_size < min_size:
            min_size = current_size
            min_cols, min_rows = found_cols, found_rows
            if min_size == 1:  
                break
                
    return min_cols, min_rows

def check_separate_combinations(cols, rows, cols_count, rows_count, ones_positions):
    for cols_combo in combinations(cols, cols_count):
        for rows_combo in combinations(rows, rows_count):
            current_cover = list(cols_combo) + list(rows_combo)
            if check_coverage(current_cover, ones_positions, cols):
                return list(cols_combo), list(rows_combo)
    return None, None

def generate_size_combinations(cols, rows, current_min):
    max_cols = len(cols)
    max_rows = len(rows)
    
    for total in range(1, max_cols + max_rows + 1):
        if total >= current_min:
            continue
        for cols_count in range(min(total, max_cols) + 1):
            rows_count = total - cols_count
            if rows_count <= max_rows and rows_count >= 0:
                yield cols_count, rows_count

def find_end_row(row: Tuple):
    block, (start_i, start_j) = row
    if isinstance(block[0], int):
        end_i = start_i
        end_j = start_j + len(block)-1
    else:
        height = len(block)
        width = len(block[0])
        end_i = start_i + height - 1
        end_j = start_j + width - 1
    return end_i, end_j

def find_end_column(column: Tuple):
    block, (start_i, start_j) = column
    if isinstance(block[0], int):
        end_i = start_i + len(block)-1
        end_j = start_j
    else: 
        height = len(block)
        width = len(block[0])
        end_i = start_i + height - 1
        end_j = start_j + width - 1
    return end_i, end_j

def find_changed_indices(arr1, arr2):    
    changed_indices = []
    for index, (elem1, elem2) in enumerate(zip(arr1, arr2)):
        if elem1 != elem2:
            changed_indices.append(index)
    return changed_indices
    
def gray_code_to_list(num: int, bits: int) -> List[int]:
    """Возвращает биты числа в коде Грея заданной длины."""
    gray = num ^ (num >> 1)
    return [(gray >> i) & 1 for i in range(bits - 1, -1, -1)]

def analyze_kmap_group(group: List[Tuple[int, int]], row_vars: str = 'ab', col_vars: str = 'cd') -> str:
    (r1, c1), (r2, c2) = group
    rows = sorted({r % 4 for r in range(r1, r2 + 1)}) 
    cols = sorted({c % 4 for c in range(c1, c2 + 1)})
    
    term = []
    for i, var in enumerate(row_vars):
        bits = [gray_code_to_list(r, len(row_vars))[i] for r in rows]
        if all(b == bits[0] for b in bits):
            term.append(f"{'' if bits[0] else '¬'}{var}")
    for i, var in enumerate(col_vars):
        bits = [gray_code_to_list(c, len(col_vars))[i] for c in cols]
        if all(b == bits[0] for b in bits):
            term.append(f"{'' if bits[0] else '¬'}{var}")
    
    return ''.join(term)

def get_minimal_dnf(groups: List[List[Tuple[int, int]]], row_vars: str = 'ab', col_vars: str = 'cd') -> str:
    terms = [analyze_kmap_group(group, row_vars, col_vars) for group in groups]
    return ' ∨ '.join(f"({t})" for t in terms) if len(terms) > 1 else terms[0]

def get_minimal_knf(groups: List[List[Tuple[int, int]]], row_vars: str = 'ab', col_vars: str = 'cd') -> str:
    terms = [analyze_kmap_group(group, row_vars, col_vars) for group in groups]
    
    knf_terms = []
    for term in terms:
        literals = []
        i = 0
        while i < len(term):
            if term[i] == '¬':
                literals.append(term[i] + term[i+1])
                i += 2
            else:
                literals.append(term[i])
                i += 1
        inverted_literals = [lit[1:] if '¬' in lit else f'¬{lit}' for lit in literals]
        knf_terms.append(f"({'∨'.join(inverted_literals)})")
    
    return ''.join(knf_terms) if len(knf_terms) > 1 else knf_terms[0]

def make_sdnf(expression, vars:List[str]):
    karno = make_karno_table(expression)
    truth_table = solve_expression(expression)
    sdnf = SOP.make_sdnf(truth_table)
    vars_col = []
    vars_col_len = len(vars)//2
    vars_row = []
    for i in range(vars_col_len):
        vars_col.append(vars[i])
    for i in range(vars_col_len, len(vars)):
        vars_row.append(vars[i])
    cols = split_columns_with_coordinates(karno)
    cols_compound_depth = compound_cols_depth(cols)
    cols_compound = compound_cols_width(cols_compound_depth)
    rows = split_rows_with_coordinates(karno)
    rows_compound_depth = compound_rows_depth(rows)
    rows_compound = compound_rows_width(rows_compound_depth)
    min_cover_separated = find_separate_cover(karno, cols_compound, rows_compound)
    separated_cols = min_cover_separated[0]
    separated_rows = min_cover_separated[1]
    start_end_array = []
    for elem in separated_cols:
        start_end_array.append([elem[1], find_end_column(elem)])
    for elem in separated_rows:
        start_end_array.append([elem[1], find_end_row(elem)])
    vars_col_str = "".join(vars_col)
    vars_row_str = "".join(vars_row)
    impl = get_minimal_dnf(start_end_array, vars_col_str, vars_row_str)
    result = sdnf_karno(sdnf, impl)
    return result

def make_sknf(expression, vars:List[str]):
    karno = make_karno_table(expression)
    karno = reverse_karno(karno)
    truth_table = solve_expression(expression)
    sknf = POS.make_sknf(truth_table)
    vars_col = []
    vars_col_len = len(vars)//2
    vars_row = []
    for i in range(vars_col_len):
        vars_col.append(vars[i])
    for i in range(vars_col_len, len(vars)):
        vars_row.append(vars[i])
    karno = reverse_karno(karno)
    cols = split_columns_with_coordinates(karno)
    cols_compound_depth = compound_cols_depth(cols)
    cols_compound = compound_cols_width(cols_compound_depth)
    rows = split_rows_with_coordinates(karno)
    rows_compound_depth = compound_rows_depth(rows)
    rows_compound = compound_rows_width(rows_compound_depth)
    min_cover_separated = find_separate_cover(karno, cols_compound, rows_compound)
    separated_cols = min_cover_separated[0]
    separated_rows = min_cover_separated[1]
    start_end_array = []
    for elem in separated_cols:
        start_end_array.append([elem[1], find_end_column(elem)])
    for elem in separated_rows:
        start_end_array.append([elem[1], find_end_row(elem)])
    vars_col_str = "".join(vars_col)
    vars_row_str = "".join(vars_row)
    impl = get_minimal_knf(start_end_array, vars_col_str, vars_row_str)
    result = sknf_karno(sknf, impl)
    return result

def reverse_karno(karno: List[List[int]]):
    result = karno.copy()
    for i in range(len(karno)):
        for j in range(len(karno[i])):
            result[i][j] = 1 - karno[i][j]
    return result
            
def get_vars(expression):
    result = set()
    for elem in expression:
        if elem.isalpha():
            result.add(elem)
    return sorted(list(result))

