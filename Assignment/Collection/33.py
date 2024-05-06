'''Write a Python program to count the number of students in an individual class.
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})'''

from collections import Counter

def count_students(tuples):
    class_counts = Counter(class_name for class_name, _ in tuples)

    return class_counts

tuples_of_tuples = (('V', [1, 2]), ('VI', [1, 2, 3]), ('VII', [1]))
result = count_students(tuples_of_tuples)
print(result)
