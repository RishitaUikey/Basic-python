'''Write a  Python program to get the frequency of elements in a given list of lists. Use the collections module.
Sample Output:
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
Frequency of the elements in the said list of lists:
Counter({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})'''

from collections import Counter

def get_frequency(list_of_lists):
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    frequency = Counter(flattened_list)

    return frequency

x = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]

frequency = get_frequency(x)
print("Frequency of the elements in the said list of lists:",frequency)

