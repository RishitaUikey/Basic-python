'''Write a Python program to initialize a list containing the numbers in the specified range where start and end are inclusive and the ratio between two terms is step. Return an error if step equals 1.
Sample Output:
[1, 2, 4, 8, 16, 32, 64, 128, 256]
[3, 6, 12, 24, 48, 96, 192]
[1, 4, 16, 64, 256]'''

def initialize_list(start, end, step):
    if step == 1:
        return "Error: Step cannot be 1"
    else:
        result = [start]
        while start * step <= end:
            start *= step
            result.append(start)
        return result

sample_range1 = (1, 300, 2)
sample_range2 = (3, 250, 2)
sample_range3 = (1, 300, 4)
result1 = initialize_list(*sample_range1)
result2 = initialize_list(*sample_range2)
result3 = initialize_list(*sample_range3)
print(result1)
print(result2)
print(result3)
