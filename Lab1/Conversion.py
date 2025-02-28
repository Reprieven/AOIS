from Operations.SumBinary import sum_binary
from typing import List

def decimal_to_bin_direct(decimal: float, digits_int: int = 8, digits_float: int = 5)->List[int]:
    res_int = [0]*digits_int
    res_fractional = []
    if decimal < 0:
        decimal = abs(decimal)
        res_int[0] = 1
    if decimal - int(decimal):
        res_fractional += [0]*digits_float
        decimal_fractional = decimal - int(decimal)
        i = 0
        while decimal_fractional!=0:
            res_fractional[i]=int(decimal_fractional*2)
            decimal_fractional = decimal_fractional*2 - int(decimal_fractional*2)
            i+=1 
    decimal_int = int(decimal)
    i = len(res_int) - 1
    while decimal_int!=0:
        if i<1 and decimal_int>0:
            print("Число вне диапазона")
            return []
        res_int[i] = decimal_int % 2
        decimal_int = decimal_int // 2
        i-=1
    return res_int+res_fractional

def decimal_to_bin_inverse(decimal: int, digits: int = 8)->List[int]:
    res = decimal_to_bin_direct(decimal, digits)
    if decimal>=0:
        return res
    else:
        for i in range(len(res)-1,0,-1):
            if res[i]==0:
                res[i] = 1
            else:
                res[i] = 0
        return res
        
def decimal_to_bin_complement(decimal: int, digits: int = 8)->List[int]:
    res = decimal_to_bin_inverse(decimal=decimal,digits=digits)
    if decimal>=0:
        return res
    else:
        one = [0]*(digits-1)+[1]
        return sum_binary(res,one)
    
def complement_to_direct(direct: List[int])->List[int]:
    res = direct
    for i in range(len(direct)-1,0,-1):
        if res[i]==0:
            res[i] = 1
        else:
            res[i] = 0
    one = [0]*(len(direct)-1)+[1]
    return sum_binary(res,one)    

def bin_to_decimal(binary: List[int])->int:
    res = 0
    is_negative = False
    if binary[0] == 1:
        is_negative = True

    for i in range(1,len(binary)):
        res += binary[i]*(2**(len(binary)-i-1))

    return -res if is_negative else res

def bin_to_decimal_fractional(binary: List[int])->float:
    res = 0
    for i in range(len(binary)):
        res += binary[i]*(2**(-i-1))
    return res

def decimal_to_bin_ieee754(decimal: float) -> List[int]:
    decimal_int = int(decimal)
    decimal_fractional = decimal - int(decimal)
    binary_int = []
    binary_fractional = []
    if decimal == 0:
        return [0]*32
    while decimal_int>0 and (len(binary_int)+len(binary_fractional))<32:
        binary_int.append(decimal_int%2)
        decimal_int = decimal_int//2
    binary_int.reverse()
    while decimal_fractional > 0 and (len(binary_int)+len(binary_fractional))<32 :
        decimal_fractional *= 2
        binary_fractional.append(int(decimal_fractional))
        decimal_fractional -= int(decimal_fractional) 
    if not binary_int:
        shift = 0
        while binary_fractional and binary_fractional[0] == 0:
            binary_fractional.pop(0)
            shift -= 1
        if not binary_fractional:
            return [0] * 32
        mantissa = binary_fractional[1:] 
        exponent = shift - 1
    else:
        mantissa = binary_int[1:] + binary_fractional
        exponent = len(binary_int) - 1
    mantissa += [0] * (23 - len(mantissa))
    exponent_value = exponent + 127
    exponent_binary = []
    while exponent_value > 0:
        exponent_binary.append(exponent_value % 2)
        exponent_value = exponent_value // 2
    exponent_binary.reverse()
    exponent_binary = [0] * (8 - len(exponent_binary)) + exponent_binary
    res = [0] + exponent_binary + mantissa
    return res[:32]

def bin_to_decimal_ieee754(binary: List[int]) -> float:
    if not any(binary):
        return 0
    exponent_binary = [0] + binary[1:9]
    exponent_value = bin_to_decimal(exponent_binary) - 127
    if exponent_value == 128:
            return "-Inf" if binary[0] else "Inf"
    mantissa_binary = [1] + binary[9:]
    mantissa_value = 0
    base = 1
    for bit in mantissa_binary:
        mantissa_value += bit * base
        base = base/2
    return mantissa_value * (2 ** exponent_value)