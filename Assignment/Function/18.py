# Write a Python program to execute a string containing Python code.

str1 = 'print("Hello World!")'
code = '''def add(a,b):
    return a+b
print("The addition of two given numbers is ",add(2,8))'''

exec(str1)
exec(code)