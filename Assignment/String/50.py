'''Write a Python program to split a string on the last occurrence of the delimiter'''

def split_on_last_occurrence(string, delimiter):
    parts = string.rsplit(delimiter, 1)
    if len(parts) == 1:
        return [string, '']
    else:
        return parts
string = "hello world, how are you, world"
delimiter = ", "
result = split_on_last_occurrence(string, delimiter)
print("Original string:", string)
print("After splitting on the last occurrence of delimiter:")
print("First part:", result[0])
print("Second part:", result[1])
