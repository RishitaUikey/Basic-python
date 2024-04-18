'''Write a  Python program to calculate the product, multiplying all the numbers in a given tuple.
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648'''

def calculate_product(t):
    result = 1
    for num in t:
        result *= num
    return result

tuples = [(4, 3, 2, 2, -1, 18), (2, 4, 8, 8, 3, 2, 9)]

for idx, t in enumerate(tuples):
    product = calculate_product(t)
    print("Product - multiplying all the numbers of the said tuple:", product)
