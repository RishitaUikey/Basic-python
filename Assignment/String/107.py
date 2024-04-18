'''Write a  Python program that takes two strings. Count the number of times each string contains the same three letters at the same index.
Sample Data:
("Red RedGreen") -> 1
("Red White Red White) -> 7
("Red White White Red") -> 0'''
def count_same_three_letters(str1, str2):
    if len(str1) != len(str2):
        return "Error: Strings must have the same length."
    count = 0
    for i in range(len(str1) - 2):
        if str1[i:i+3] == str2[i:i+3]:
            count += 1       
    return count
samples = [
    ("Red RedGreen"),
    ("Red White Red White"),
    ("Red White White Red")
]
for sample in samples:
    strings = sample.split()
    if len(strings) != 2:
        print("Invalid sample data.")
        continue
    str1, str2 = strings
    print(f'("{str1}", "{str2}") -> {count_same_three_letters(str1, str2)}')
