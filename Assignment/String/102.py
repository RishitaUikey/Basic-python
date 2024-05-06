'''Write a  Python program to remove punctuation from a given string.
Sample Output:
Original text:
String! With. Punctuation?
After removing Punctuations from the said string:
String With Punctuation'''
import string

def remove_punctuation(text):
    punctuations = set(string.punctuation)
    text_without_punctuation = ''.join(char for char in text if char not in punctuations)
    
    return text_without_punctuation
original_text = "String! With. Punctuation?"
text_without_punctuation = remove_punctuation(original_text)
print("Original text:")
print(original_text)
print("After removing Punctuations from the said string:")
print(text_without_punctuation)
