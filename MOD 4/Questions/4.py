"""
Create an Abstract Base Class called Shape that includes abstract methods:
- area()
- circumference()

Then derive two classes Circle and Rectangle from the Shape class 
and implement the area() and circumference() methods.

Write a Python program to implement the above concept.
"""

from abc import ABC
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def
