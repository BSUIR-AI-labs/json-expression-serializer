def is_letter(expression: str):
    return expression.lower() in 'qwertyuiopasdfghjklzxcvbnm'

def is_number(expression: str) -> bool:
    try:
        num = float(expression)
        return True
    except:
        return False


def is_symbol(expression: str) -> bool:
    return expression in "+-/*()=^."


def valid_all_nums(expression: str) -> str:
    num = ''
    is_num = False
    to_replace = []
    for i in range(len(expression)):
        if expression[i] == '.':
            num += '.'
            continue
        if is_number(expression[i]):
            if not is_num: first = i
            if i > 1 and not is_num and expression[i - 1] == '-' and is_symbol(expression[i - 2]):
                num += '-'
            num += expression[i]
            is_num = True
        else:
            if is_num:
                is_num = False
                to_replace.append(f'({num})')
                num = ''
            if (expression[i] == '-' 
                and i + 1 < len(expression) 
                and is_number(expression[i + 1])
                and (i == 0 or not (is_letter(expression[i-1]) or expression[i-1] in ")"))):
                continue
            to_replace.append(expression[i])

    result = ''
    for token in to_replace: result += token
    if num: result += f'({num})'
    return result


def make_all_operations(expression: str) -> str:
    if not expression: return ''
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


def all_brackets_are_closed(expression: str) -> bool:
    depth = 0
    for i in range(len(expression)):
        if expression[i] == '(': depth += 1
        if expression[i] == ')':
            if depth == 0: return False
            depth -= 1
    return depth == 0



def all_binary_operations_are_valid(expression: str) -> bool:
    for i in range(len(expression)):
        if expression[i] in "+/*^":
            if i == 0 or i == len(expression) - 1: return False
            if (
                not is_number(expression[i - 1]) and
                not is_letter(expression[i - 1]) and
                expression[i - 1] != ")"
            ): return False
            if (
                not is_number(expression[i + 1]) and
                not is_letter(expression[i + 1]) and
                expression[i + 1] not in "(-"
            ): return False
    if expression[len(expression) - 1] == '-': return False
    return True



def has_one_equal(expression: str) -> bool:
    return (expression.count('=') == 1 
            and expression[0] != '=' 
            and expression[len(expression) - 1] != '=')


def has_only_valid_symbols(expression: str) -> bool:
    for token in expression:
        if (
            not (
                is_number(token) or
                is_letter(token) or
                is_symbol(token)
                )
        ): return False
    return True


def all_dots_are_correct(expression: str) -> bool:
    was_dot_only = False
    for i in range(len(expression)):
        if expression[i] == '.':
            if i == 0 or i == len(expression) - 1: return False
            if not is_number(expression[i - 1]) or not is_number(expression[i + 1]): return False
            if was_dot_only: return False
            was_dot_only = True
        if expression[i] in "+-/*^":
            was_dot_only = False
    return True


def has_variables_or_numbers(expression: str) -> bool:
    for token in expression:
        if is_number(token) or is_letter(token):
            return True
    return False



def is_correct_expression(expression: str) -> bool:
    return (
        expression and
        all_brackets_are_closed(expression) and
        all_binary_operations_are_valid(expression) and
        has_one_equal(expression) and
        has_only_valid_symbols(expression) and
        all_dots_are_correct(expression) and
        has_variables_or_numbers(expression)
    )