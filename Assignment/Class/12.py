'''Write a  Python class named Student with two instances student1, student2 and assign values to the instances' attributes. 
Print all the attributes of the student1, student2 instances with their values in the given format.'''

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

print("Attributes and values of student1:")
for attr, value in student1.__dict__.items():
    print(f"{attr}: {value}")

print("\nAttributes and values of student2:")
for attr, value in student2.__dict__.items():
    print(f"{attr}: {value}")
