def is_letter(expression: str):
    return expression.lower() in 'qwertyuiopasdfghjklzxcvbnm'

def is_number(expression: str) -> bool:
    try:
        num = float(expression)
        return True
    except:
        return False


def is_symbol(expression: str) -> bool:
    return expression in "+-/*()^"


def valid_all_nums(expression: str) -> str:
    num = ''
    is_num = False
    to_replace = []
    for i in range(len(expression)):
        if expression[i] == '.':
            num += '.'
            continue
        if is_number(expression[i]):
            if i > 1 and not is_num and expression[i - 1] == '-' and is_symbol(expression[i - 2]):
                num += '-'
            num += expression[i]
            is_num = True
        else:
            if is_num:
                is_num = False
                to_replace.append(num)
                num = ''
    for exp in to_replace: expression = expression.replace(exp, f"({exp})")
    return expression


def make_all_operations(expression: str) -> str:
    validated_expression = ''
    i = 0
    expression = valid_all_nums(expression)
    while i < len(expression) - 1:
        if i == 0:
            if expression[i] == '-' and not is_number(expression[i + 1]): validated_expression += "(-1)*"
            else: validated_expression += expression[i]
            i += 1
            continue
        if expression[i] == '-':
            if expression[i - 1] == '(' or expression[i - 1] in "+-*/^=": validated_expression += "(-1)*"
            else: validated_expression += '-'
            i += 1
            continue
        if (is_letter(expression[i - 1]) or expression[i - 1] == ')') and (is_letter(expression[i]) or expression[i] == '('):
            validated_expression += '*' + expression[i]
            i += 1
            continue
        if expression[i - 1] == ')' and expression[i] == '(':
            validated_expression += '*' + expression[i]
            i += 1
            continue 
        validated_expression += expression[i]
        i += 1
    validated_expression += expression[len(expression) - 1]
    return validated_expression
