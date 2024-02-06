# Write a Python program to remove characters that have odd index values in a given string.

given_str = input("Enter the String: ")
result = ''
for index,char in enumerate(given_str):
    if index % 2 == 0:
        result += char
print(result)
    