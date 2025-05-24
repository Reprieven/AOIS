from i_calc_method import *
from trigger_condition import find_trigger_conditions

bits = {"a":[0,1,0,1,0,1,0,1],
        "b":[0,0,1,1,0,0,1,1],
        "c":[0,0,0,0,1,1,1,1]
        }

result = find_trigger_conditions(bits)
print(result)
