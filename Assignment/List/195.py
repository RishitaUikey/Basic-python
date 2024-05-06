'''Write a  Python program to traverse a given list in reverse order, and print the elements with the original index.
Original list:
['red', 'green', 'white', 'black']
Traverse the said list in reverse order:
black
white
green
red
Traverse the said list in reverse order with original index:
3 black
2 white
1 green
0 red'''

def traverse_reverse_with_index(lst):
    n = len(lst)
    for i, elem in enumerate(reversed(lst)):
        print(n - 1 - i, elem)

original_list = ['red', 'green', 'white', 'black']
print("Original list:")
print(original_list)
print("Traverse the said list in reverse order:")
for elem in reversed(original_list):
    print(elem)

print("Traverse the said list in reverse order with original index:")
traverse_reverse_with_index(original_list)
