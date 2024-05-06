'''Write a Python program to create two empty classes, Student and Marks. Now create some 
instances and check whether they are instances of the said classes or not. Also, check 
whether the said classes are subclasses of the built-in object class or not.'''

class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()

print("Is student_instance an instance of Student class?", isinstance(student_instance, Student))
print("Is marks_instance an instance of Marks class?", isinstance(marks_instance, Marks))

print("Is Student class a subclass of object class?", issubclass(Student, object))
print("Is Marks class a subclass of object class?", issubclass(Marks, object))
