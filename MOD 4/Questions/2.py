from math import gcd

# Question:
# 3. Write a Python program to create a class called Rational to model rational numbers
#    and associated operations. Implement the following methods:
#    - Reduce() to return the simplified fraction form.
#    - add_() to add two rational numbers.
#    - __gt__() to compare two rational numbers using the less-than operator.
# Use operator overloading to perform these operations.

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()  # Simplify the fraction immediately upon creation

    # Method to simplify the fraction
    def reduce(self):
        common_gcd = gcd(self.numerator, self.denominator) # Calculate the GCD
        self.numerator //= common_gcd # Simplify the numerator
        self.denominator //= common_gcd

    # Overloading the + operator to add two rational numbers
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)
    # a/b + c/d => (a*d + b*c) / (b*d)


    # Overloading the < operator to compare two rational numbers (less than operation)
    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator
    # a/b < c/d => a*d < b*c

    # Overloading the __str__ method for printing the rational number
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Test the Rational class
rational1 = Rational(1, 2)  # 1/2
rational2 = Rational(3, 4)  # 3/4

# Add two rational numbers
result_add = rational1 + rational2
print(f"Addition: {result_add}")  # Expected output: 5/4

# Compare two rational numbers
print(f"Is {rational1} greater than {rational2}? {rational1 > rational2}")  # Expected output: True
