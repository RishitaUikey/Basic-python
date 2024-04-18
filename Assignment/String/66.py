'''Write a  Python program to make two given strings (lower case, may or may not be of the same length) 
anagrams without removing any characters from any of the strings.'''

def make_anagrams(str1, str2):
    count1 = {char: str1.count(char) for char in set(str1)}
    count2 = {char: str2.count(char) for char in set(str2)}
    for char in count1:
        count2[char] = count2.get(char, 0) - count1[char]
    for char in count2:
        count1[char] = count1.get(char, 0) - count2[char]
    new_str1 = ''.join([char * count1[char] for char in sorted(count1)])
    new_str2 = ''.join([char * count2[char] for char in sorted(count2)])

    return new_str1, new_str2
string1 = "listen"
string2 = "silent"
new_string1, new_string2 = make_anagrams(string1, string2)
print("Anagram of first string:", new_string1)
print("Anagram of second string:", new_string2)

