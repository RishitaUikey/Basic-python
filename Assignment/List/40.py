# Write a Python program to split a list based on the first character of a word.

word_list = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'giraffe','horse','indri','jellyfish','kangroo','lion']
split_result = {}
for word in word_list:
    first_char = word[0]
    if first_char in split_result:
        split_result[first_char].append(word)
    else:
        split_result[first_char] = [word]

for first_char, words in split_result.items():
    print(f"Words starting with '{first_char}': {words}")
