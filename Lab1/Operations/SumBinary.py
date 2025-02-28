from typing import List
def sum_binary(first: List[int], second: List[int])->List[int]:
    if len(first)>len(second):
        digits = len(first)
    else:
        digits = len(second)
    res = [0]*digits
    carry = 0
    for i in range(len(res)-1,-1,-1):
        sum = first[i]+second[i]+carry
        carry = sum // 2
        res[i] = sum % 2
    return res