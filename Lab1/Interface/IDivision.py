from Conversion import decimal_to_bin_direct
from Conversion import decimal_to_bin_inverse
from Conversion import decimal_to_bin_complement
from Operations.Division import division
def division_interface():
    print("Деление:")
    print("Ввод числа №1:")
    first = int(input())
    print(f"Число введено: {first}")
    print(f"Прямой код: {decimal_to_bin_direct(first)}")
    print(f"Обратный код: {decimal_to_bin_inverse(first)}")
    print(f"Дополнительный код: {decimal_to_bin_complement(first)}")
    print("Ввод числа №2:")
    second = int(input())
    print(f"Число введено: {second}")
    print(f"Прямой код: {decimal_to_bin_direct(second)}")
    print(f"Обратный код: {decimal_to_bin_inverse(second)}")
    print(f"Дополнительный код: {decimal_to_bin_complement(second)}")
    result_decimal = division(first,second)
    if result_decimal != "Inf":
        print(f"Результат: {result_decimal}")
        print(f"Прямой код: {decimal_to_bin_direct(result_decimal,16)}")
    else:
        print("Нельзя делить на 0")
