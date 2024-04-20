'''Write a Python program that fills a list with the specified value.
Sample Output:
[0, 0, 0, 0, 0, 0, 0]
[3, 3, 3, 3, 3, 3, 3, 3]
[-2, -2, -2, -2, -2]
[3.2, 3.2, 3.2, 3.2, 3.2]'''

def fill_list(value, length):
    return [value] * length

sample_value1 = 0
sample_length1 = 7
sample_value2 = 3
sample_length2 = 8
sample_value3 = -2
sample_length3 = 5
sample_value4 = 3.2
sample_length4 = 5

result1 = fill_list(sample_value1, sample_length1)
result2 = fill_list(sample_value2, sample_length2)
result3 = fill_list(sample_value3, sample_length3)
result4 = fill_list(sample_value4, sample_length4)
print(result1)
print(result2)
print(result3)
print(result4)
