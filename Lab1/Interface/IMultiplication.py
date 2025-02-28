from Conversion import decimal_to_bin_direct
from Conversion import decimal_to_bin_inverse
from Conversion import decimal_to_bin_complement
from Operations.Multiplication import multiplication
def multiplication_interface():
    print("Умножение:")
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
    result_decimal = multiplication(first,second)
    print(f"Результат: {result_decimal}")
    print(f"Прямой код: {decimal_to_bin_direct(result_decimal,16)}")
    print(f"Обратный код: {decimal_to_bin_inverse(result_decimal,16)}")
    print(f"Дополнительный код: {decimal_to_bin_complement(result_decimal,16)}")