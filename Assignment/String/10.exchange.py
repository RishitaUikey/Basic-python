'''Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.'''

str = 'Nikita'
result = str[-1] + str[1:-1] + str[0]
print(result)