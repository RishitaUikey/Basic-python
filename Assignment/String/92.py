'''Write a  Python program to find string similarity between two given strings.
Sample Output:
Original string:
Python Exercises
Python Exercises
Similarity between two said strings:
1.0
Original string:
Python Exercises
Python Exercise
Similarity between two said strings:
0.967741935483871
Original string:
Python Exercises
Python Ex.
Similarity between two said strings:
0.6923076923076923
Original string:
 Python Exercises
Python
Similarity between two said strings:
0.5454545454545454
Original string:
Java Exercises
Python
Similarity between two said strings:
0.0'''


def string_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union

    return similarity

sample_strings = [
    ("Python Exercises", "Python Exercises"),
    ("Python Exercises", "Python Exercise"),
    ("Python Exercises", "Python Ex."),
    (" Python Exercises", "Python"),
    ("Java Exercises", "Python")
]

for str1, str2 in sample_strings:
    print("Original strings:")
    print(str1)
    print(str2)
    print("Similarity between two strings:")
    print(string_similarity(str1, str2))
    print()

