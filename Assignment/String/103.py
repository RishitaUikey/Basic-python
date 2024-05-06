'''Write a  Python program to replace each character of a word of length five and more with a hash character (#).
Sample Output:
Original string: Count the lowercase letters in the said list of words:
Replace words (length five or more) with hash characters in the said string:
##### the ######### ####### in the said list of ######
Original string: Python - Remove punctuations from a string:
Replace words (length five or more) with hash characters in the said string:
###### - ###### ############ from a #######
'''
def replace_long_words_with_hashes(text):
    words = text.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = '#' * len(words[i])
    return ' '.join(words)

input1 = "Count the lowercase letters in the said list of words:"
input2 = "Python - Remove punctuations from a string:"

output1 = replace_long_words_with_hashes(input1)
output2 = replace_long_words_with_hashes(input2)

print("Original string:", input1)
print("Replace words (length five or more) with hash characters in the said string:")
print(output1)

print("\nOriginal string:", input2)
print("Replace words (length five or more) with hash characters in the said string:")
print(output2)
