'''  Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"  '''

def reverse_string(s_string):
    
    for i in s_string:
        i = s_string[::-1]
    return i
my_string = "1234abcd"
output = reverse_string(my_string)
print("The reverse string is ",output)