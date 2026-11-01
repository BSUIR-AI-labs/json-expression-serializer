import parsing as p
import json
from validation import is_correct_expression, make_all_operations

def main(expression: str, n: int) -> dict:
    expression = make_all_operations(expression.replace(" ", ""))
    if is_correct_expression(expression):
        parsed_expression = p.parse_expression(expression)
        json_file = json.dumps(parsed_expression, indent=4)
        with open(f'./output/result_{n}.json', 'w', encoding='utf-8') as f:
            f.write(json_file)
    else:
        print(f"Expression {n} is invalid")