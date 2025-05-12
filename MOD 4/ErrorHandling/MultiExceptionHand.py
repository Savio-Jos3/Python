try:
    x = int(input("Enter a number: "))
    result = 10 / x  # Might raise ZeroDivisionError or ValueError
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")
else:
    print(f"Result is {result}")
finally:
    print("Execution completed.")
