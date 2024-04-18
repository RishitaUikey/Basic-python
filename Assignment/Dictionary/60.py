'''Write a  Python program to find the shortest list of values for the keys in a given dictionary.
Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']'''

def shortest_lists(dictionary):
    min_length = min(len(values) for values in dictionary.values())
    shortest_keys = [key for key, values in dictionary.items() if len(values) == min_length]
    
    return shortest_keys

original_dict = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

result = shortest_lists(original_dict)
print("Shortest list of values with the keys of the said dictionary:")
print(result)
