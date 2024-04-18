'''Write a  Python program to print the following integers with '*' to the right of the specified width.'''

def print_integers_with_star_padding(numbers, width):
    for number in numbers:
        print(f"{number:<{width}}*")

numbers = [123, 456, 789]
width = 6
print_integers_with_star_padding(numbers, width)
