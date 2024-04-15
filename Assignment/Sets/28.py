# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

from itertools import combinations

def find_combinations(numbers, target):
    result = []
    for combination in combinations(numbers, 3):
                
        if sum(combination) == target:
            result.append(combination)
    return result

numbers = [2, 3, 4, 5, 6, 7]
target_sum = 12

combinations = find_combinations(numbers, target_sum)

print("Unique combinations of 3 numbers adding up to", target_sum, ":")
for combo in combinations:
    print(combo)
