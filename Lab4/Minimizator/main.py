from SOP import make_sdnf
from ICalcMethod import *
truth_table_bi ={
    "a":[0,0,0,0,1,1,1,1],
    "b":[0,0,1,1,0,0,1,1],
    "c":[0,1,0,1,0,1,0,1],
    "res":[0,1,1,1,0,0,0,1]
}
truth_table_d = {
    "a":[0,0,0,0,1,1,1,1],
    "b":[0,0,1,1,0,0,1,1],
    "c":[0,1,0,1,0,1,0,1],
    "res":[0,1,1,0,1,0,0,1]
}

truth_table_W = {
    "a":[0,0,0,0,0,0,0,0,1,1],
    "b":[0,0,0,0,1,1,1,1,0,0],
    "c":[0,0,1,1,0,0,1,1,0,0],
    "d":[0,1,0,1,0,1,0,1,0,1],
    "res":[0,0,0,0,0,0,1,1,1,1]
}

truth_table_X = {
    "a":[0,0,0,0,0,0,0,0,1,1],
    "b":[0,0,0,0,1,1,1,1,0,0],
    "c":[0,0,1,1,0,0,1,1,0,0],
    "d":[0,1,0,1,0,1,0,1,0,1],
    "res":[0,0,1,1,1,1,0,0,0,0]
}

truth_table_Y = {
    "a":[0,0,0,0,0,0,0,0,1,1],
    "b":[0,0,0,0,1,1,1,1,0,0],
    "c":[0,0,1,1,0,0,1,1,0,0],
    "d":[0,1,0,1,0,1,0,1,0,1],
    "res":[1,1,0,0,1,1,0,0,1,1]
}

truth_table_Z = {
    "a":[0,0,0,0,0,0,0,0,1,1],
    "b":[0,0,0,0,1,1,1,1,0,0],
    "c":[0,0,1,1,0,0,1,1,0,0],
    "d":[0,1,0,1,0,1,0,1,0,1],
    "res":[0,1,0,1,0,1,0,1,0,1]
}


sdnf_bi = make_sdnf(truth_table_bi)
sdnf_di = make_sdnf(truth_table_d)
sdnf_interface_calc(sdnf_bi)
sdnf_interface_calc(sdnf_di)


sdnf_W = make_sdnf(truth_table_W)
sdnf_X = make_sdnf(truth_table_X)
sdnf_Y = make_sdnf(truth_table_Y)
sdnf_Z = make_sdnf(truth_table_Z)

print("СДНФ W")
sdnf_interface_calc(sdnf_W)
print("СДНФ X")
sdnf_interface_calc(sdnf_X)
print("СДНФ Y")
sdnf_interface_calc(sdnf_Y)
print("СДНФ Z")
sdnf_interface_calc(sdnf_Z)
