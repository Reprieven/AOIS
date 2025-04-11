from typing import List
def bin_to_decimal(binary: List[int])->int:
    res = 0
    for i in range(0,len(binary)):
        res += binary[i]*(2**(len(binary)-i-1))
    return res
