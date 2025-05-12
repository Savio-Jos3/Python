try:
    # Example: Dividing by zero
    num = 10
    result = num / 0

except ZeroDivisionError:
    print("Cannot divide by zero!")
    
try:
    # Example: TypeError
    result = "hello" + 10
    
except TypeError:
    print("You cannot concatenate a string and an integer!")

try:
    # Example: FileNotFoundError
    with open("non_existent_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("The file you're trying to open does not exist!")

try:
    # Example: ValueError
    num = int("hello")
    
except ValueError:
    print("Invalid input! Cannot convert 'hello' to an integer.")
