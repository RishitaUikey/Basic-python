'''Write a  Python program to create a dictionary with the unique values of a given list as keys and their frequencies as values.
Sample Output:
{'a': 4, 'b': 2, 'f': 2, 'c': 1, 'e': 2}
{3: 4, 4: 2, 7: 1, 5: 2, 9: 1, 0: 1, 2: 1}'''

def frequency_dictionary(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
sample_list1 = ['a', 'b', 'a', 'c', 'e', 'f', 'a', 'f']
sample_list2 = [3, 4, 7, 3, 5, 9, 3, 4, 5, 0, 3, 2]
freq_dict1 = frequency_dictionary(sample_list1)
freq_dict2 = frequency_dictionary(sample_list2)
print(freq_dict1)
print(freq_dict2)
