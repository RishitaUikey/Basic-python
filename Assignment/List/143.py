''' Write a  Python program to get the frequency of elements in a given list of lists.
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
Frequency of the elements in the said list of lists:
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}'''

def frequency_of_elements(list_of_lists):
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    frequency_dict = {}
    for element in flattened_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    return frequency_dict

list_of_lists = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
frequency = frequency_of_elements(list_of_lists)
print("Frequency of the elements in the said list of lists:")
print(frequency)
