'''Write a  Python program to find the maximum length of consecutive 0's in a given binary string.'''

def max_consecutive_zeros(binary_string):
    max_zeros = 0
    current_zeros = 0

    for char in binary_string:
        if char == '0':
            current_zeros += 1
            max_zeros = max(max_zeros, current_zeros)
        else:
            current_zeros = 0

    return max_zeros

# Example usage:
binary_string = "110100011000"
max_zeros = max_consecutive_zeros(binary_string)
print("Maximum length of consecutive zeros:", max_zeros)
