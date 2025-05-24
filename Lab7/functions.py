from operations import *
def f4(first_address, second_address): #Запрет 2-го аргумента
    result = [0]*len(first_address)
    for i in range(len(first_address)):
        result[i] = conjunction(inversion(first_address[i]), second_address[i])
    return result

def f6(first_address, second_address): #Неравнозначность
    result = [0]*len(first_address)
    for i in range(len(first_address)):
        result[i] = 1 - equivalence(first_address[i], second_address[i])
    return result

def f9(first_address, second_address):#Эквивалентность
    result = [0]*len(first_address)
    for i in range(len(first_address)):
        result[i] = equivalence(first_address[i], second_address[i])
    return result

def f11(first_address, second_address):#Импликация от второго аргумента
    result = [0]*len(first_address)
    for i in range(len(first_address)):
        result[i] = implication(second_address[i], first_address[i])
    return result

