'''Write a Python program to convert a given string list to a tuple.
Original string:  python 3.0
<class 'str'>
Convert the said string to a tuple:
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<class 'tuple'>'''

s = "python 3.0"
tuple_from_string = tuple(s)
print("Type of original string:", type(s))
print("Converted string to a tuple:", tuple_from_string)
print("Type of converted tuple:", type(tuple_from_string))
