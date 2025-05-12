class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)
    
    def __str__(self):
        return f"{self.pages} pages"

book1 = Book(100)
book2 = Book(150)

total = book1 + book2 # book1.__add__(book2)
print(total)  # Output: 250 pages
# The __add__ method allows us to use the + operator to add two Book objects together.
# The __str__ method allows us to define how the object should be represented as a string.
