''' Write a Python function to get a string made of 4 copies of the last two characters 
of a specified string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses'''

def copies_of_last_two_characters(str):
    last_two = str[-2:]
    return last_two * 4

print(copies_of_last_two_characters('Python'))
print(copies_of_last_two_characters('Exercises'))