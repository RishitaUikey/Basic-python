'''Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.
The original list, tuple :
[(2, 7), (2, 6), (1, 8), (4, 9)]
Maximum and minimum product from the pairs of the said tuple of list:
(36, 8)'''

def max_min_product(list_of_tuples):
    max_product = float('-inf')
    min_product = float('inf')

    for tuple_pair in list_of_tuples:
        product = tuple_pair[0] * tuple_pair[1]
        max_product = max(max_product, product)
        min_product = min(min_product, product)

    return max_product, min_product

list_of_tuples = [(2, 7), (2, 6), (1, 8), (4, 9)]

max_product, min_product = max_min_product(list_of_tuples)

print("The original list, tuple :")
print(list_of_tuples)
print("Maximum and minimum product from the pairs of the said tuple of list:")
print((max_product, min_product))
