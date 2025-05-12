from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Concrete class implementing abstract method
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# ----------- Using the classes -----------
d = Dog()
c = Cat()
d.make_sound()  # Output: Bark
c.make_sound()  # Output: Meow
