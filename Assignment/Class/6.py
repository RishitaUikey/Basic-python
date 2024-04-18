'''Write a  Python function student_data () that will print the ID of a student (student_id). 
If the user passes an argument student_name or student_class the function will print the 
student name and class.'''

def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name is not None and student_class is not None:
        print("Student Name:", student_name)
        print("Student Class:", student_class)

student_data(123)
print()
student_data(456, "Alice", "Grade 10")
