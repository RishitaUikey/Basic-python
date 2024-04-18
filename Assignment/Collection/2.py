'''Write a  Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]'''

from collections import Counter

def most_common(text, n=3):
    counts = Counter(text)
    most_common_elements = counts.most_common(n)
    return most_common_elements

text = "lkseropewdssafsdfafkpwe"
most_common_chars = most_common(text)
print("Most common three characters of the said string:",most_common_chars)
