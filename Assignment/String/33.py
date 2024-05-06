'''Write a  Python program to print the following integers with zeros to the left of the specified width.'''

def print_integers_with_zero_padding(numbers, width):
    for number in numbers:
        print(f"{number:0{width}d}")
numbers = [123, 456, 789]
width = 6
print_integers_with_zero_padding(numbers, width)
