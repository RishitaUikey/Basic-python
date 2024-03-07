'''Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.'''

def palindrome(s):
    
    return s == s[::-1]
input_str = input("Enter the string to check :")
if palindrome(input_str):
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")



