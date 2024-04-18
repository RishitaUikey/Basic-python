'''Write a  Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}'''

s = 'w3resource'
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
