'''Write a Python program to display a number in left, right, and center aligned with a width of 10.'''

def display_aligned_numbers(number):
    left_aligned = "{:<10}".format(number)
    print("Left aligned:", left_aligned)
    right_aligned = "{:>10}".format(number)
    print("Right aligned:", right_aligned)
    center_aligned = "{:^10}".format(number)
    print("Center aligned:", center_aligned)

number = 123
display_aligned_numbers(number)
