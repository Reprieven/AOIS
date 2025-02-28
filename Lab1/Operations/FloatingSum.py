from Conversion import decimal_to_bin_ieee754
from Operations.SumBinary import sum_binary
from typing import List
def bits_regain(first: List[int], second: List[int]) -> List[int]:
    len_diff = abs(len(first) - len(second))
    if len(first) > len(second):
        second = [0] * len_diff + second
    else:
        first = [0] * len_diff + first
        
    return first, second

def bin_to_decimal(binary: List[int])->int:
    res = 0
    for i in range(len(binary)):
        res += binary[i]*(2**(len(binary)-i-1))

    return res

def sum_ieee754(first: float,second: float) -> List[int]:
    if not first:
        return second
    if not second:
        return first
    first_binary = decimal_to_bin_ieee754(first)
    second_binary = decimal_to_bin_ieee754(second)
    exponent1_bin =  first_binary[1:9]
    exponent2_bin =  second_binary [1:9]
    mantis_1 = [1]+first_binary[9:]
    mantis_2 = [1]+second_binary[9:]
    exponent1 = bin_to_decimal(exponent1_bin)
    exponent2 = bin_to_decimal(exponent2_bin)
    dif = abs(exponent1 - exponent2)
    if exponent1>exponent2:
        exponent = exponent1
        exponent_bin = exponent1_bin
    else:
        exponent = exponent2
        exponent_bin = exponent2_bin
    while dif:
        if exponent == exponent1:
            mantis_2 = mantis_2[:-1]
        else:
            mantis_1 = mantis_1[:-1]
        dif-=1
    mantis_1,mantis_2 = bits_regain(mantis_1,mantis_2)
    res = [0] * len(mantis_1)
    carry = 0
    for i in range(len(res)-1,-1,-1): 
        sum = mantis_1[i]+mantis_2[i]+carry
        res[i] = sum%2
        carry = sum//2
    if carry:
        res = res[:23]
    else:
        res = res[1:24]
    if carry:
        exponent_bin,carry = bits_regain(exponent_bin,[carry])
        exponent_bin = sum_binary(carry,exponent_bin)
    res_binary =  [0]+exponent_bin+res
    return res_binary

