# Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_prefix(strings):
    if not strings:
        return ""  
    
    for i, char in enumerate(strings[0]):
            if any(s[i] != char for s in strings[1:]):
                return strings[0][:i]  
    return strings[0]  

words = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_prefix(words))
