'''Write a  Python program to count the most and least common characters in a given string.
Sample Output:
Original string:
hello world
Most common character of the said string: l
Least common character of the said string: h'''

from collections import Counter

original_string = "hello world"
char_counts = Counter(original_string)
most_common_char = char_counts.most_common(1)[0][0]
least_common_char = char_counts.most_common()[-1][0]

print("Most common character of the said string:", most_common_char)
print("Least common character of the said string:", least_common_char)
