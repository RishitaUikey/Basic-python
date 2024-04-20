'''Write a  Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
Original lists:
[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
Consecutive duplicate elements and their frequency:
([1, 2, 4, 5], [1, 3, 3, 4])'''

def count_consecutive_duplicates(lst):
    consecutive_duplicates = []
    frequencies = []

    current_element = None
    current_frequency = 0

    for num in lst:
        if num == current_element:
            current_frequency += 1
        else:
            if current_element is not None:
                consecutive_duplicates.append(current_element)
                frequencies.append(current_frequency)
            current_element = num
            current_frequency = 1

    if current_element is not None:
        consecutive_duplicates.append(current_element)
        frequencies.append(current_frequency)
    return consecutive_duplicates, frequencies

original_list = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
consecutive_duplicates, frequencies = count_consecutive_duplicates(original_list)

print("Original list:")
print(original_list)
print("Consecutive duplicate elements and their frequency:")
print(consecutive_duplicates, frequencies)
