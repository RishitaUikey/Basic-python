'''Write a  Python program to find the longest common sub-string from two given strings.'''

def longest_common_substring(str1, str2):

    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    max_length = 0 
    end_index = 0 

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_index = i
            else:
                matrix[i][j] = 0

    start_index = end_index - max_length
    return str1[start_index:end_index]
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = longest_common_substring(str1, str2)
print("Longest common substring:", result)
