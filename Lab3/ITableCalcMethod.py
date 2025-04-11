from TableCalcMethod import *
from ParserSDNF import separate_terms_sdnf
from ParseSKNF import separate_terms_sknf, delete_plus
from Calc import calc_SDNF,calc_SKNF
from ICalcMethod import replace_upper_case_with_inversion, add_disjunction
from prettytable import PrettyTable


def show_table_sdnf(expression: str): 
    table = PrettyTable()
    consts = separate_terms_sdnf(expression)
    table.field_names = ["Конституэнты"] + consts
    terms = form_table_sdnf(expression)

    for key, value in terms.items():
        row = [key]+terms[key]
        table.add_row(row)
    print(table)

def calc_result_sdnf(expression: str): 
    table = table_calc_sdnf(expression)
    iterations = calc_SDNF(expression)
    terms = iterations[-1]
    for key in list(terms.keys()):
        if key not in table:
            terms.pop(key)
    return terms

def sdnf_interface_table_calc(expression: str): 
    show_table_sdnf(expression)
    terms= calc_result_sdnf(expression)
    keys = terms.keys()
    terms_str = "v".join(f"({key})" for key in keys)
    terms_str = replace_upper_case_with_inversion(terms_str)
    print(terms_str)

def show_table_sknf(expression: str): 
    table = PrettyTable()
    consts = separate_terms_sknf(expression)
    consts = delete_plus(consts)
    table.field_names = ["Конституэнты"] + consts
    terms = form_table_sknf(expression)

    for key, value in terms.items():
        row = [key]+terms[key]
        table.add_row(row)
    print(table)

def calc_result_sknf(expression: str): 
    table = table_calc_sknf(expression)
    iterations = calc_SKNF(expression)
    terms = iterations[-1]
    for key in list(terms.keys()):
        if key not in table:
            terms.pop(key)
    return terms

def sknf_interface_table_calc(expression: str): 
    show_table_sknf(expression)
    terms= calc_result_sknf(expression)
    keys = terms.keys()
    terms_str = "".join(f"({key})" for key in keys)
    terms_str = add_disjunction(terms_str)
    terms_str = replace_upper_case_with_inversion(terms_str)
    print(terms_str)

