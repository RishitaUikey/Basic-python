'''Write a Python program to build a list, using an iterator function and an initial seed value.
Sample Output:
[-10, -20, -30, -40]'''

def iterator_function(seed, step, length):
    for i in range(length):
        yield seed + i * step

seed_value = -10
step_value = -10
list_length = 4

result_list = list(iterator_function(seed_value, step_value, list_length))
print(result_list)
