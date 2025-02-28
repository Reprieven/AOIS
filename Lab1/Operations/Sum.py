from typing import List
from Conversion import decimal_to_bin_complement
from Conversion import complement_to_direct
from Conversion import bin_to_decimal
from Operations.SumBinary import sum_binary

def sum(first:int, second:int)->int:
    first_binary = decimal_to_bin_complement(first)
    second_binary = decimal_to_bin_complement(second)
    sum = sum_binary(first_binary,second_binary)
    if first+second < 0:
        res = complement_to_direct(sum)
    else:
        res = sum
    return bin_to_decimal(res)