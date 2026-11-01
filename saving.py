def save_as_file(expression: str) -> str:
    with open(f'./output/result.json', 'w', encoding='utf-8') as f:
        f.write(expression)