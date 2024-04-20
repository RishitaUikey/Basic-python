'''Write a Python program to extract the nth element from a given list of tuples.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Extract nth element ( n = 0 ) from the said list of tuples:
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
Extract nth element ( n = 2 ) from the said list of tuples:
[99, 96, 94, 98]'''

def extract_nth_element(lst, n):
    return [t[n] for t in lst]

original_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n = 0
result_n0 = extract_nth_element(original_list, n)
n = 2
result_n2 = extract_nth_element(original_list, n)
print("Original list:")
print(original_list)
print("Extract nth element (n = 0):")
print(result_n0)
print("Extract nth element (n = 2):")
print(result_n2)
