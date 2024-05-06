'''Write a  Python program that capitalizes the first letter and lowercases the remaining letters in a given string.
Sample Data:
("Red Green WHITE") -> "Red Green White"
("w3resource") -> "W3resource"
("dow jones industrial average") -> "Dow Jones Industrial Average"'''
def capitalize_first_letter(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

samples = [
    "Red Green WHITE",
    "w3resource",
    "dow jones industrial average"
]

for sample in samples:
    print(f'Original: "{sample}"')
    print(f'Capitalized: "{capitalize_first_letter(sample)}"\n')
