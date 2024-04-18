'''Write a  Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original and modified 
values of the said attributes.'''

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("Alice", 80)

print("Original values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)

student.student_name = "Bob"
student.marks = 90

print("\nModified values:")
print("Student Name (modified):", student.student_name)
print("Marks (modified):", student.marks)
