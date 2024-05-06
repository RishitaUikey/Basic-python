'''Write a  Python program to remove specific words from a given list.
Original list:
['red', 'green', 'blue', 'white', 'black', 'orange']
Remove words:
['white', 'orange']
After removing the specified words from the said list:
['red', 'green', 'blue', 'black']'''

def remove_words(original_list, words_to_remove):
    return [word for word in original_list if word not in words_to_remove]

original_list = ['red', 'green', 'blue', 'white', 'black', 'orange']
words_to_remove = ['white', 'orange']
print("Original list:")
print(original_list)
print("Remove words:")
print(words_to_remove)
print("After removing the specified words from the said list:")
print(remove_words(original_list, words_to_remove))
