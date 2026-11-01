from validation import is_number

def get_priority_operation(expression: str) -> int:
    depth = 0
    multiple_or_dividing_index = -1
    for i in range(len(expression) - 1, 0, -1):
        if expression[i] == ')': depth += 1
        if expression[i] == '(': depth -= 1
        if expression[i] in "+-" and depth == 0: return i
        if (expression[i] in '*/' 
            and depth == 0 
            and multiple_or_dividing_index == -1): 
                multiple_or_dividing_index = i
    if multiple_or_dividing_index != -1: return multiple_or_dividing_index
    depth = 0
    for i in range(len(expression)):
        if expression[i] == ')': depth += 1
        if expression[i] == '(': depth -= 1
        if expression[i] == "^" and depth == 0: return i
    return -1


def erase_extra_brackets(expression: str) -> str:
    while len(expression) >= 2 and expression[0] == '(' and expression[-1] == ')':
        depth = 0
        wraps = True
        for i in range(len(expression)):
            if expression[i] == '(': depth += 1
            elif expression[i] == ')': depth -= 1
            if depth == 0 and i != len(expression) - 1:
                wraps = False
                break
        if not wraps: break
        expression = expression[1:-1]
    return expression


def valid_element(expression: str) -> str:
    if len(expression) == 1 or is_number(expression): return expression
    if expression[0] == '(': expression = expression[1:]
    if expression[len(expression) - 1] == ')': expression = expression[:len(expression) - 1]
    return parse_expression(expression)



def parse_expression(expression: str, depth = 0) -> str:
    tab = '\t' * depth
    tab_inner = '\t' * (depth + 1)
    if '=' in expression:
        left, right = expression.split("=")
        left_str = parse_expression(left, depth + 2)
        right_str = parse_expression(right, depth + 2)
        return (
            f'{tab}{{\n'
            f'{tab_inner}"=": [\n'
            f'{left_str},\n'
            f'{right_str}\n'
            f'{tab_inner}]\n'
            f'{tab}}}'
        )
    if get_priority_operation(expression) == -1 and ('(' in expression or ")" in expression):
        expression = erase_extra_brackets(expression)
    operand_index = get_priority_operation(expression)
    if operand_index == -1:
        return tab + f'"{valid_element(expression)}"'
    op = expression[operand_index]
    left, right = expression[:operand_index], expression[operand_index + 1:]
    left_str = parse_expression(left, depth + 2)
    right_str = parse_expression(right, depth + 2)
    return (
        f'{tab}{{\n'
        f'{tab_inner}"{op}": [\n'
        f'{left_str},\n'
        f'{right_str}\n'
        f'{tab_inner}]\n'
        f'{tab}}}'
    )
    


