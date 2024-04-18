# Write a Python program to create a class and display the namespace of that class.

class MyClass:
    class_variable = "I am a class variable"

    def __init__(self):
        self.instance_variable = "I am an instance variable"

def display_namespace(class_obj):
    for name in dir(class_obj):
        print(name)

print("Namespace of the MyClass class:")
display_namespace(MyClass)
