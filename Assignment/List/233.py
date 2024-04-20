'''Write a  Python program to chunk a given list into n smaller lists.
Sample Output:
[[1, 2], [3, 4], [5, 6], [7]]'''

def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]
sample_list = [1, 2, 3, 4, 5, 6, 7, 8]
chunked_list = chunk_list(sample_list, 3)
print(chunked_list)

