class NegativeNumberError(Exception):
    pass

def process_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    else:
        print(f"Processing number: {num}")

try:
    process_number(-5)
except NegativeNumberError as e:
    print(f"Error: {e}")
