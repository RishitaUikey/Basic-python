'''Write a  Python program that takes a string and replaces all the characters with their respective numbers.
Sample Data:
("Python") -> "16 25 20 8 15 14"
("Java") -> "10 1 22 1"
("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"'''
def replace_with_numbers(text):
    char_to_num = {char: str(ord(char.lower()) - ord('a') + 1) for char in 'abcdefghijklmnopqrstuvwxyz'}
    
    result = ''
    for char in text:
        if char.lower() in char_to_num:
            result += char_to_num[char.lower()] + ' '
    
    return result.strip()
samples = [
    "Python",
    "Java",
    "Python Tutorial"
]
for sample in samples:
    print(f'("{sample}") -> "{replace_with_numbers(sample)}"')
