''' Write a  Python program to convert a given tuple of positive integers into an integer.
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570'''

def tuple_to_integer(t):
    return int(''.join(map(str, t)))
tuples = ((1, 2, 3), (10, 20, 40, 5, 70))
for t in tuples:
    integer_value = tuple_to_integer(t)
    print("Convert the said tuple of positive integers into an integer:", integer_value)
