class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def area(self):
        print("Area of circle: πr²")

class Square(Shape):
    def area(self):
        print("Area of square: side²")

s = Shape()
s.area()  # Output: Calculating area...

s = Circle()
s.area()  # Output: Area of circle: πr² 
s = Square()    
s.area()  # Output: Area of square: side²
# This code demonstrates polymorphism by calling the same method `area` on different objects.

'''shapes = [Circle(), Square()]

for s in shapes:
    s.area()
# This code demonstrates polymorphism by calling the same method `area` on different objects.
# Each object has its own implementation of the method, allowing for different behaviors.'''