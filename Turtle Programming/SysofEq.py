class Employee:
    def __init__(self, name="John Doe", salary=50000):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")

# Creating an object with default values
e1 = Employee()
e1.display()

# Creating an object with custom values
e2 = Employee("Alice", 70000)
e2.display()
