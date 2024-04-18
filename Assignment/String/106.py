'''Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
Sample Data:
("Red Green White") -> "Red Gren White"
("aabbbcdeffff") -> "abcdef"
("Yellowwooddoor") -> "Yelowodor"'''
def remove_repeated_characters(text):
    result = ''
    i = 0
    while i < len(text):
        result += text[i]
        j = i + 1
        while j < len(text) and text[j] == text[i]:
            j += 1
        i = j
    
    return result
samples = [
    "Red Green White",
    "aabbbcdeffff",
    "Yellowwooddoor"
]

for sample in samples:
    print(f'Original: "{sample}"')
    print(f'Updated: "{remove_repeated_characters(sample)}"\n')
