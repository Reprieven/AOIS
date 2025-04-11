from lab2.SumBinary import sum_binary
import re
def simplify_inversion(expression: str) -> str:
    simplified = re.sub(
        r'(!+)([a-zA-Z])', 
        lambda m: '!' + m.group(2) if len(m.group(1)) % 2 == 1 else m.group(2), expression
    )
    return simplified

def parser(expression: str):
    expression = simplify_inversion(expression)
    result = []
    expression = expression.replace('->','>')
    expression = expression.replace(' ','')
    for element in expression:
        result.append(element)
    return result