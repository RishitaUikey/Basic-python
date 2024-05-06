'''Write a  Python program to calculate the product of the unique numbers in a given list.
Original List : [10, 20, 30, 40, 20, 50, 60, 40]
Product of the unique numbers of the said list: 720000000'''

def product_of_unique_numbers(nums):
    unique_nums = set(nums)
    product = 1
    for num in unique_nums:
        product *= num
    return product

original_list = [10, 20, 30, 40, 20, 50, 60, 40]

result = product_of_unique_numbers(original_list)

print("Original List:", original_list)
print("Product of the unique numbers of the said list:", result)
