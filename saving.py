import tomllib

def save_as_file(expression: str) -> None:
    with open("./config.toml", "rb") as f:
        data = tomllib.load(f)
    with open(data["output"]["path"], "w", encoding=data["output"]["encoding"]) as f:
        f.write(expression)