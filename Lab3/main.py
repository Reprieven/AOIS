from ICalcMethod import sdnf_interface_calc,sknf_interface_calc
from ITableCalcMethod import sdnf_interface_table_calc, sknf_interface_table_calc
from TableMethod import *
from lab2 import POS, SOP, ValueFinder
from ViewKarno import *
expression = "(!a|!b|!c|!d)&(a|b|c|d)"
truth_table = ValueFinder.solve_expression(expression)
karno = make_karno_table(expression)
for row in karno:
    print(row)
sdnf = SOP.make_sdnf(truth_table)
sknf = POS.make_sknf(truth_table)
sdnf_interface_calc(sdnf)
sknf_interface_calc(sknf)
print("Таблично-расчетный метод")
sdnf_interface_table_calc(sdnf)
sknf_interface_table_calc(sknf)
print("Табличный метод(Карта Карно)")
print_karno_gray(karno)
result_sdnf = make_sdnf(expression, get_vars(expression))
result_sknf = make_sknf(expression, get_vars(expression))
print(result_sdnf)
print(result_sknf)

