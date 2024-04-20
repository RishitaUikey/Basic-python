'''Write a  Python program to split a given list into specified-sized chunks.
Original list:
[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
Split the said list into equal size 3
[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
Split the said list into equal size 4
[[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
Split the said list into equal size 5
[[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]'''

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

original_list = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
chunk_size = 3
result = split_list(original_list, chunk_size)
print(f"Split the said list into equal size {chunk_size}:")
print(result)
chunk_size = 4
result = split_list(original_list, chunk_size)
print(f"Split the said list into equal size {chunk_size}:")
print(result)
chunk_size = 5
result = split_list(original_list, chunk_size)
print(f"Split the said list into equal size {chunk_size}:")
print(result)
