from Operations.FloatingSum import sum_ieee754
from Conversion import bin_to_decimal_ieee754
from Conversion import decimal_to_bin_ieee754
def floating_sum_interface():
    print("Сложение с плавающей точкой:")
    print("Ввод числа №1:")
    first = float(input())
    print(decimal_to_bin_ieee754(first))
    print("Ввод числа №2:")
    second = float(input())
    print(decimal_to_bin_ieee754(second))
    result_bin = sum_ieee754(first,second)
    print(f"Результат: {bin_to_decimal_ieee754(result_bin)}")
    print(f"В виде ieee754: {result_bin}")