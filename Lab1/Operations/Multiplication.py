from Conversion import decimal_to_bin_direct
from Conversion import bin_to_decimal
def multiplication(first:int, second: int)->int:
    is_negative = (first < 0) != (second < 0)
    first_abs = abs(first)
    second_abs = abs(second)
    first_binary = decimal_to_bin_direct(first_abs)
    second_binary = decimal_to_bin_direct(second_abs)
    res_binary = [0]*(len(first_binary)+len(second_binary))
    for i in range(len(second_binary)-1,-1,-1):
        if second_binary[i] == 1:
            carry = 0
            for j in range(len(first_binary)-1,-1,-1):
                sum = first_binary[j]+res_binary[i+j+1]+carry
                carry = sum // 2
                res_binary[i+j+1]=sum%2
            res_binary[i + j] += carry
    res_decimal = bin_to_decimal(res_binary)       
    return -res_decimal if is_negative else res_decimal