'''Write a  Python program to sort a given positive number in descending/ascending order.
Descending -> Highest to lowest.
Ascending -> Lowest to highest
Original Number: 134543
Descending order of the said number: 544331
Ascending order of the said number: 133445
Original Number: 43750973
Descending order of the said number: 97754330
Ascending order of the said number: 3345779'''

def sort_number(num):
    num_str = str(num)
    digits = list(num_str)
    sorted_desc = ''.join(sorted(digits, reverse=True))
    sorted_asc = ''.join(sorted(digits))
    return int(sorted_desc), int(sorted_asc)

original_number1 = 134543
desc1, asc1 = sort_number(original_number1)
print("Original Number:", original_number1)
print("Descending order of the said number:", desc1)
print("Ascending order of the said number:", asc1)

original_number2 = 43750973
desc2, asc2 = sort_number(original_number2)
print("Original Number:", original_number2)
print("Descending order of the said number:", desc2)
print("Ascending order of the said number:", asc2)
