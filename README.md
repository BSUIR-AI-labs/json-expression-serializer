# JSON Expression Serializer

Parser of arithmetic expressions with saving into JSON-file with structure saving.

## How To Use It?

*You need to download Python 3.11+ first. You can do it with (Example for Linux):*
```bash
sudo apt install python3
```

1. Clone the repo:
```bash
git clone https://github.com/BSUIR-AI-labs/json-expression-serializer.git
cd json-expression-serializer
```

2. Edit `config.toml`:
```toml
[output]
path = "./output/result.json"
encoding = "utf-8"
```

3. Open `main.py` and write the expression in the `main(...)` call. **Example**:
```python
main("a+b=c")
```

4. Run `main.py`:
```bash
python3 main.py
```


## Example Of Using

Serializer will create a file with structure like this:
```json
{
	"=": [
		{
			"+": [
				"a",
				"b"
			]
		},
		"c"
	]
}