'''Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.
Sample Output:
42
Error in input!
Error in input!'''
def add_strings_as_numbers(str1, str2):
    if not str1.isdigit() or not str2.isdigit():
        return "Error in input!"
    result = int(str1) + int(str2)
    return str(result)
input1 = "42"
input2 = "23"

print(add_strings_as_numbers(input1, input2))  

input3 = "42"
input4 = "abc"
print(add_strings_as_numbers(input3, input4)) 
