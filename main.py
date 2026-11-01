import parsing as p
import validation as v
import saving as s

def main(expression: str) -> dict:
    expression = v.make_all_operations(expression.replace(" ", ""))
    if v.is_correct_expression(expression):
        parsed_expression = p.parse_expression(expression)
        s.save_as_file(parsed_expression)
    else:
        print(f"Expression is invalid")