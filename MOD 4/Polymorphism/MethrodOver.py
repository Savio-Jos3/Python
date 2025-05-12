class Calculator:
    # Simulating overloaded add() method
    def add(self, a=0, b=0, c=0):
        return a + b + c

# Create object
calc = Calculator()

# Call method with different number of arguments
print("Sum of 2 and 3:", calc.add(2, 3))           # Output: 5
print("Sum of 1, 2 and 3:", calc.add(1, 2, 3))      # Output: 6
print("Sum with no arguments:", calc.add())        # Output: 0
