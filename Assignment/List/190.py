'''Write a  Python program to find the specified number of largest products from two given lists, multiplying an element from each list.
Original lists:
[1, 2, 3, 4, 5, 6]
[3, 6, 8, 9, 10, 6]
3 Number of largest products from the said two lists:
[60, 54, 50]
4 Number of largest products from the said two lists:
[60, 54, 50, 48]'''

def largest_products(list1, list2, n):
    products = [x * y for x in list1 for y in list2]
    largest = sorted(products, reverse=True)[:n]
    return largest

list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 6, 8, 9, 10, 6]
n = 3
print(f"Original lists:")
print(list1)
print(list2)
print(f"{n} Number of largest products from the said two lists:")
print(largest_products(list1, list2, n))
n = 4
print(f"\nOriginal lists:")
print(list1)
print(list2)
print(f"{n} Number of largest products from the said two lists:")
print(largest_products(list1, list2, n))
