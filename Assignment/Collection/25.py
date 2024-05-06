'''Write a  Python program to find the characters in a list of strings that occur more or less than a given number.
Sample Output:
Original list:
['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
Characters of the said list of strings which occur more than: 3
['a', 'd', 'f']
Characters of the said list of strings which occur less than: 3
['c', 'b', 'h', 'e', 'i', 's', 'l', 'k', 'j', 'g']'''

from collections import Counter


x= ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
number = 3
flat= ''.join(x)
char_counts = Counter(flat)

more_than_given = [char for char, count in char_counts.items() if count > number]
less_than_given = [char for char, count in char_counts.items() if count < number]

print("Characters of the said list of strings which occur more than:", number)
print(more_than_given)

print("Characters of the said list of strings which occur less than:", number)
print(less_than_given)
