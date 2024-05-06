'''Write a  Python program to capitalize the first and last letters of each word in a given string.'''

def capitalize_first_and_last(string):
    words = string.split() 
    result = [] 
    for word in words:
        modified_word = word[0].upper() + word[1:-1] + word[-1].upper()
        result.append(modified_word)
    return ' '.join(result)

input_string = input("Enter a string: ")
result_string = capitalize_first_and_last(input_string)
print("Modified string:", result_string)
