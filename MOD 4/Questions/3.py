# Question:
# 4. What is exception handling in Python? Write a program that opens a file and writes
#    "Hello, Good morning" to it. Handle exceptions that can be generated during file I/O operations.
try:
    # Attempt to open the file in write mode
    file = open('example.txt', 'w')  # Open the file 'example.txt' for writing
    file.write("Hello, Good morning!")  # Write the string to the file
    print("Successfully wrote to the file.")  # This will print if no errors occur
except FileNotFoundError:
    print("Error: The file could not be found.")  # This will handle if the file is not found
except IOError:
    print("Error: An I/O error occurred.")  # This handles any I/O errors (e.g., file permissions)
except Exception as e:
    print(f"An unexpected error occurred: {e}")  # This will handle any unexpected errors
finally:
    print("Execution completed.")  # This will always execute, whether or not an error occurs
