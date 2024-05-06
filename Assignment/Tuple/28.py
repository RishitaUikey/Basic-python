'''Write a  Python program to convert a tuple of string values to a tuple of integer values.
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))'''

t = (('333', '33'), ('1416', '55'))
new_tuple = tuple((int(x), int(y)) for x, y in t)
print("New tuple values:",new_tuple)
