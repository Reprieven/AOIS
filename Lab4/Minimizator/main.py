from SOP import make_sdnf
from ICalcMethod import *
from truth_table_maker import *
truth_table_bi = generate_bi()
truth_table_d =  generate_d()

table_8421 = generate_plus_2_table()


sdnf_bi = make_sdnf(truth_table_bi)
sdnf_di = make_sdnf(truth_table_d)
sdnf_interface_calc(sdnf_bi)
sdnf_interface_calc(sdnf_di)

for item in table_8421.items():
    print(item)
