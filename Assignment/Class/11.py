'''Write a Python class named Student with two attributes: student_id, student_name. 
Add a new attribute: student_class. Create a function to display all attributes and 
their values in the Student class.'''

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_attributes(self):
        attributes = vars(self)
        print("Attributes and their values:")
        for attr, value in attributes.items():
            print(f"{attr}: {value}")

student = Student(123, "Alice")
student.student_class = "Grade 10"

student.display_attributes()
