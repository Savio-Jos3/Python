# Question:
# 1. Write a Python program to create a class called Complex to model complex numbers.
# Implement the following methods:
#   - __add__() for adding two complex numbers using the + operator.
#   - __mul__() for multiplying two complex numbers using the * operator.
# Display the result by overloading the + and * operators.

class Complex:
    def __init__(self, real, imag):
        self.real = real  # Real part of the complex number
        self.imag = imag  # Imaginary part of the complex number

    # Overloading the + operator
    def __add__(self, other):
        # Adding the real and imaginary parts separately
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)

    # Overloading the * operator
    def __mul__(self, other):
        # Multiplying complex numbers (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    # Overloading the __str__ method to return the complex number in a readable format
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Test the Complex class
complex1 = Complex(3, 4)  # 3 + 4i
complex2 = Complex(1, 2)  # 1 + 2i

# Add two complex numbers
result_add = complex1 + complex2 # complex1.__add__(complex2)
# The __add__ method is called when using the + operator
print(f"Addition: {result_add}")  # Expected output: 4 + 6i

# Multiply two complex numbers
result_mul = complex1 * complex2 # complex1.__mul__(complex2)
# The __mul__ method is called when using the * operator
print(f"Multiplication: {result_mul}")  # Expected output: -5 + 10i
