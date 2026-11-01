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
    depth = 0
    first_bracket = 0
    while first_bracket < len(expression) and expression[first_bracket] != '(': first_bracket += 1
    expression_copy = expression[first_bracket:len(expression) - 1]
    for i in range(len(expression_copy)):
        if expression_copy[i] == '(': depth += 1
        if expression_copy[i] == ')': depth -= 1
    if depth == 0: return expression_copy
    return expression


def valid_element(expression: str) -> any:
    if len(expression) == 1 or is_number(expression): return expression
    if expression[0] == '(': expression = expression[1:]
    if expression[len(expression) - 1] == ')': expression = expression[:len(expression) - 1]
    return parse_expression(expression)



def parse_expression(expression: str) -> any:
    if '=' in expression:
        print(expression)
        left, right = expression.split("=")
        return {"=": [parse_expression(left), parse_expression(right)]}
    if get_priority_operation(expression) == -1 and ('(' in expression or ")" in expression):
        expression = erase_extra_brackets(expression) 
    operand_index = get_priority_operation(expression)
    if operand_index == -1: 
        return valid_element(expression)
    left, right = expression[:operand_index], expression[operand_index + 1: ] 
    return {expression[operand_index]: [parse_expression(left), parse_expression(right)]}
    


