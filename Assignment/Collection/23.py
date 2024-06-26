'''Write a  Python program to get the frequency of the tuples in a given list.
Sample Output:
Original list of tuples:
[(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
Tuples frequency
('1', '4') 2
('3', '4') 1
('2', '7') 2
('6', '8') 2
('5', '8') 1
('5', '7') 1'''

from collections import Counter

o = [(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
flattened = [tuple(item) for sublist in o for item in sublist]
tuple_counts = Counter(flattened)


print("Tuples frequency")
for tup, freq in tuple_counts.items():
    print(tup, freq)
