# Write a Python program to access a function inside a function.

def func(a):
    def func2(b):
        nonlocal a
        a +=1
        return a+b
    return func2
output = func(5)
print(output(5))