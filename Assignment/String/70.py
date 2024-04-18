'''Write a  Python program that concatenates uncommon characters from two strings.'''

def uncommon_characters(str1, str2):
    uncommon_chars = ""
    count1 = {char: str1.count(char) for char in set(str1)}
    count2 = {char: str2.count(char) for char in set(str2)}
    for char in count1:
        if char not in count2:
            uncommon_chars += char
    for char in count2:
        if char not in count1:
            uncommon_chars += char
    return uncommon_chars
string1 = "hello"
string2 = "world"
result = uncommon_characters(string1, string2)
print("Uncommon characters:", result)
