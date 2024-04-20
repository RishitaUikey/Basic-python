'''Write a  Python program to remove words from a given list of strings containing a character or string.
Original list:
list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
Character list:
['#', 'color', '@']
New list:
['Red', '', 'Green', 'Orange', 'White']'''

def remove_words_with_chars(strings, char_list):
    new_list = []
    for string in strings:
        for char in char_list:
            string = string.replace(char, '')
        new_list.append(string.strip())
    return new_list

list1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
char_list = ['#', 'color', '@']

new_list = remove_words_with_chars(list1, char_list)

print("Original list:")
print("list1:", list1)
print("Character list:")
print(char_list)
print("New list:")
print(new_list)
