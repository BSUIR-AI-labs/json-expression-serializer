import parsing as p
import  json

def main(expression: str, n: int) -> dict:
    parsed_expression = p.parse_expression(expression)
    json_file = json.dumps(parsed_expression, indent=4)
    with open(f'./output/result_{n}.json', 'w', encoding='utf-8') as f:
        f.write(json_file)