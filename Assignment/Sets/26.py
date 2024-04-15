# Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.

def group_anagrams(strings):
    anagram_groups = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))  
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    return list(anagram_groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_groups = group_anagrams(words)

print("Anagram groups:")
for group in anagram_groups:
    print(group)
