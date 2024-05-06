'''Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def count_letters(str):
    count_upper = 0
    count_lower = 0
    for char in str:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    return  count_upper,count_lower 

my_str = 'The quick Brow Fox'
count_upper,count_lower = count_letters(my_str)
print("Number of uppercase letters: ",count_upper)
print("Number of lowercase letters: ",count_lower)  