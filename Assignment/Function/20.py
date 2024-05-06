# Write a Python program to detect the number of local variables declared in a function.

def func():
    a ,b,c,d = 1,2,3,4
    print("Python Function")
print(func.__code__.co_nlocals)