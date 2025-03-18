from ICalcMethod import sdnf_interface_calc,sknf_interface_calc
from ITableCalcMethod import sdnf_interface_table_calc, sknf_interface_table_calc
sdnf = "(¬a¬bc) ∨ (¬ab¬c) ∨ (¬abc) ∨ (a¬b¬c) ∨ (a¬bc) ∨ (ab¬c)"
sknf = "(¬a+¬b+¬c)(a+b+c)"
sdnf_interface_calc(sdnf)
sknf_interface_calc(sknf)
sdnf_interface_table_calc(sdnf)
sknf_interface_table_calc(sknf)

