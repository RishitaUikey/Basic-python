'''Write a  Python program to get the weighted average of two or more numbers.
Sample Output:
Original list elements:
[10, 50, 40]
[2, 5, 3]
Weighted average of the said two list of numbers:
39.0
Original list elements:
[82, 90, 76, 83]
[0.2, 0.35, 0.45, 32]
Weighted average of the said two list of numbers:
82.97272727272727'''

def weighted_average(numbers, weights):
    total = sum(num * weight for num, weight in zip(numbers, weights))
    total_weights = sum(weights)
    return total / total_weights

sample_lists_numbers = [
    [10, 50, 40],
    [82, 90, 76, 83]
]
sample_lists_weights = [
    [2, 5, 3],
    [0.2, 0.35, 0.45, 32]
]

for numbers, weights in zip(sample_lists_numbers, sample_lists_weights):
    print("Original list elements:")
    print(numbers)
    print(weights)
    print("Weighted average of the said two list of numbers:")
    print(weighted_average(numbers, weights))

