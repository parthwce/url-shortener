# url-shortener

## Expected Behavior

- The program should print a friendly error like "Error: Code not found."
- It should not crash or throw exceptions.

## Actual Behavior

- The program throws a Python `KeyError` exception and crashes.

## Suggested Fix

- Add a check if the code exists before returning the URL.
- Print an informative error message if code not found.

## Environment

- Python 3.6+
- OS: Any
# url-shortener

A simple URL shortener in Python.

## How to Use
```bash
python url_shortener.py shorten https://google.com
python url_shortener.py expand <short_code>



