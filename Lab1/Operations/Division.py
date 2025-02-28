from Conversion import decimal_to_bin_direct
from Conversion import bin_to_decimal
from Conversion import decimal_to_bin_direct 
from Conversion import bin_to_decimal_fractional
from typing import List
from Operations.Subtraction import subtraction
def bits_regain(binary :List[int])->List[int]:
    while len(binary)<8:
        binary = [0]+binary
    return binary

def bits_shorten(binary: List[int], length: int)->list[int]:
    while len(binary)>length:
        binary.pop(0)
    return binary

def division(first: int, second: int)->int:
    try:
        first/second
    except ZeroDivisionError:
        return "Inf"
    is_negative = (first < 0) != (second < 0)
    first_abs = abs(first)
    second_abs = abs(second)
    first_binary = decimal_to_bin_direct(first_abs)
    second_binary = decimal_to_bin_direct(second_abs)
    res_binary_int = []
    dividend_bits = [0]
    for i in range(len(first_binary)):
        dividend_bits.append(first_binary[i])
        regained_dividend_bin = bits_regain(dividend_bits)
        regained_dividend_decimal = bin_to_decimal(regained_dividend_bin)
        if second_abs <= regained_dividend_decimal:
            res_binary_int.append(1)
            dividend_bits = decimal_to_bin_direct(subtraction(regained_dividend_decimal,second_abs))
            bits_shorten(dividend_bits,i)
        else:
            res_binary_int.append(0)

    res_binary_fractional = []
    for i in range(5):
        dividend_bits.append(0)
        regained_dividend_bin = bits_regain(dividend_bits)
        regained_dividend_decimal = bin_to_decimal(regained_dividend_bin)
        if second_abs <= regained_dividend_decimal:
            res_binary_fractional.append(1)
            dividend_bits = decimal_to_bin_direct(subtraction(regained_dividend_decimal,second_abs))
            bits_shorten(dividend_bits,len(second_binary))
        else:
            res_binary_fractional.append(0)
    res_decimal_int = bin_to_decimal(res_binary_int)
    res_decimal_fractional = bin_to_decimal_fractional(res_binary_fractional)
    res = res_decimal_int+res_decimal_fractional
    return -res if is_negative else res

