'''Write a  Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result:
243'''

def round_and_sum(numbers):
    rounded_sum = sum(round(num) for num in numbers)
    return rounded_sum * len(numbers)

original_list = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
result = round_and_sum(original_list)
print("Original list:", original_list)
print("Result:", result)
