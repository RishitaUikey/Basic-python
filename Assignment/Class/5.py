# Define a  Python function student(). Using function attributes display the names of all arguments.

def student(name, age, grade):
    pass

print("Names of all arguments:")
print(student.__code__.co_varnames[:student.__code__.co_argcount])
