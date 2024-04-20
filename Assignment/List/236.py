'''Write a  Python program to find items that are parity outliers in a given list.
Sample Output:
[1, 3]
[2, 4, 6]'''

def parity_outliers(lst):
    evens = [num for num in lst if num % 2 == 0]
    odds = [num for num in lst if num % 2 != 0]
    majority_parity = evens if len(evens) > len(odds) else odds
    outliers = [num for num in lst if num not in majority_parity]
    return majority_parity, outliers

sample_list = [1, 3, 4, 6, 2, 8]
majority_parity, outliers = parity_outliers(sample_list)
print(outliers)
print(majority_parity)

