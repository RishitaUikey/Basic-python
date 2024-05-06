''' Write a Python program that accepts a hyphen-separated sequence of words as input 
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

def hyphen_separated_sequence(words):
    word_list = words.split('-')
    sorted_list = sorted(word_list)
    return '-'.join(sorted_list)
Sample_Items = "green-red-yellow-black-white"
output = hyphen_separated_sequence(Sample_Items)
print("Expected Result: ",output)