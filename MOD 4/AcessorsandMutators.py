class Student:
    def __init__(self, name):
        self.name = name
    def getStudentName(self):# Acessor
        return self.name
    def setStudentName(self, name): # Mutator
        self.name = name

s1 = Student("John")
s1.setStudentName("Doe")
print(s1.getStudentName())  # Output: Doe   

print(s1.getStudentName())
# Output: Doe