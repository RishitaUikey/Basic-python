'''Write a Python program to find all the common characters in lexicographical order from two given lower case strings.
If there are no similar letters print "No common characters".'''
def common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_chars = sorted(set1.intersection(set2))
    
    if not common_chars:
        return "No common characters"
    else:
        return ''.join(common_chars)

# Example usage:
string1 = "hello"
string2 = "world"
result = common_characters(string1, string2)
print("Common characters:", result)
