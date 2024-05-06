'''Write a  Python class named Student with two attributes student_id, student_name. Add a new attribute student_class 
and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire 
attribute with values.'''

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student = Student(123, "Alice")

student.student_class = "Grade 10"

print("All attributes and their values:")
print(student.__dict__)

del student.student_name

print("\nRemaining attributes and their values:")
print(student.__dict__)
