'''Write a  Python program to convert a given list of tuples to a list of strings.
Original list of tuples:
[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
Convert the said list of tuples to a list of strings:
['red green', 'black white', 'orange pink']
Original list of tuples:
[('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
Convert the said list of tuples to a list of strings:
['Laiba Delacruz', 'Mali Stacey Drummond', 'Raja Welch', 'Saarah Stone']'''

def tuples_to_strings(lst):
    return [' '.join(tup) for tup in lst]
original_list1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
print("Original list of tuples:")
print(original_list1)
print("Convert the said list of tuples to a list of strings:")
print(tuples_to_strings(original_list1))

original_list2 = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
print("\nOriginal list of tuples:")
print(original_list2)
print("Convert the said list of tuples to a list of strings:")
print(tuples_to_strings(original_list2))
