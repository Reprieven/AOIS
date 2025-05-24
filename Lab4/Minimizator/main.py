from SOP import make_sdnf
from ICalcMethod import *
from truth_table_maker import *
truth_table_bi = generate_bi()
truth_table_d =  generate_d()

table_8421 = generate_plus_2_table()


sdnf_bi = make_sdnf(truth_table_bi)
sdnf_di = make_sdnf(truth_table_d)
print("ДНФ bi")
sdnf_interface_calc(sdnf_bi)
print("ДНФ di")
sdnf_interface_calc(sdnf_di)


for item in table_8421.items():
    print(item)

w_table = {"w": [], "x": [], "y": [], "z": [], "res": []}
x_table = {"w": [], "x": [], "y": [], "z": [], "res": []}
y_table = {"w": [], "x": [], "y": [], "z": [], "res": []}
z_table = {"w": [], "x": [], "y": [], "z": [], "res": []}

for i in range(10):
    w_table["w"].append(table_8421["W"][i])
    w_table["x"].append(table_8421["X"][i])
    w_table["y"].append(table_8421["Y"][i])
    w_table["z"].append(table_8421["Z"][i])
    w_table["res"].append(table_8421["W'"][i])
    
    x_table["w"].append(table_8421["W"][i])
    x_table["x"].append(table_8421["X"][i])
    x_table["y"].append(table_8421["Y"][i])
    x_table["z"].append(table_8421["Z"][i])
    x_table["res"].append(table_8421["X'"][i])
    
    y_table["w"].append(table_8421["W"][i])
    y_table["x"].append(table_8421["X"][i])
    y_table["y"].append(table_8421["Y"][i])
    y_table["z"].append(table_8421["Z"][i])
    y_table["res"].append(table_8421["Y'"][i])
    
    z_table["w"].append(table_8421["W"][i])
    z_table["x"].append(table_8421["X"][i])
    z_table["y"].append(table_8421["Y"][i])
    z_table["z"].append(table_8421["Z"][i])
    z_table["res"].append(table_8421["Z'"][i])

w_table_sdnf = make_sdnf(w_table)
x_table_sdnf = make_sdnf(x_table)
y_table_sdnf = make_sdnf(y_table)
z_table_sdnf = make_sdnf(z_table)


print("ДНФ w")
sdnf_interface_calc(w_table_sdnf)
print("ДНФ x")
sdnf_interface_calc(x_table_sdnf)
print("ДНФ y")
sdnf_interface_calc(y_table_sdnf)
print("ДНФ z")
sdnf_interface_calc(z_table_sdnf)



