'''Write a  Python program to find the common values that appear in two given strings.
Sample Output:
Original strings:
 Python3
Python2.7
Intersection of two said String:
Python'''
def common_values(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_set = set1.intersection(set2)
    common_string = ''.join(common_set)

    return common_string
str1 = "Python3"
str2 = "Python2.7"

print("Original strings:")
print(str1)
print(str2)

result = common_values(str1, str2)

print("Intersection of two said String:")
print(result)
