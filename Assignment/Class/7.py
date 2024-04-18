'''Write a simple Python class named Student and display its type. Also, display the 
__dict__ attribute keys and the value of the __module__ attribute of the Student class.'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Alice", 20)

print("Type of Student class:", type(Student))
print("Keys of __dict__ attribute of Student class:", Student.__dict__.keys())
print("Value of __module__ attribute of Student class:", Student.__module__)


