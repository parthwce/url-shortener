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



