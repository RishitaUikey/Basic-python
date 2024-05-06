'''Write a  Python program to count the lowercase letters in a given list of words.
Sample Data:
(["Red", "Green", "Blue", "White"]) -> 13
(["SQL", "C++", "C"]) -> 0'''

def count_lowercase_letters(word_list):
    count = 0
    for word in word_list:
        count += sum(1 for char in word if char.islower())
    return count

sample_data = [
    ["Red", "Green", "Blue", "White"],
    ["SQL", "C++", "C"]
]

for words in sample_data:
    print(count_lowercase_letters(words))