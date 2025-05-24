from typing import List

def sum_binary(first: List[int], second: List[int])->List[int]:
    first_five =[0]+first.copy()
    second_five = [0]+second.copy()
    res = [0]*len(first_five)
    carry = 0
    for i in range(len(res)-1,-1,-1):
        sum = first_five[i]+second_five[i]+carry
        carry = sum // 2
        res[i] = sum % 2
    return res