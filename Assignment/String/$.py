'''Write a Python program to get a string from a given string where all occurrences of its first 
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t' '''

u_string = 'restart'
first_char = u_string[0]
expected_result = first_char + u_string[1:].replace(first_char,'$')

print("Expected_Result:",expected_result)


