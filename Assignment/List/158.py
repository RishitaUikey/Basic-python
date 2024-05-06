'''Write a  Python program to find the maximum and minimum values in a given list of tuples.
Original list with tuples:
[('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
Maximum and minimum values of the said list of tuples:
(78, 60)'''

def find_max_min(list_of_tuples):
    if not list_of_tuples:
        return None, None

    max_val = min_val = list_of_tuples[0][1] 
    for _, value in list_of_tuples:
        if value > max_val:
            max_val = value
        elif value < min_val:
            min_val = value
    return max_val, min_val

original_list = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
max_value, min_value = find_max_min(original_list)
print("Maximum and minimum values of the said list of tuples:")
print((max_value, min_value))
