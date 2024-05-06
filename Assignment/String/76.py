'''Write a Python program to count the number of substrings from a given string of 
lowercase alphabets with exactly k distinct (given) characters.'''

def count_k_distinct_substrings(input_string, k):
    count = 0
    distinct_count = 0
    frequency = [0] * 26  
    left = 0
    for right in range(len(input_string)):
        if frequency[ord(input_string[right]) - ord('a')] == 0:
            distinct_count += 1
        frequency[ord(input_string[right]) - ord('a')] += 1
        while distinct_count > k:
            frequency[ord(input_string[left]) - ord('a')] -= 1
            if frequency[ord(input_string[left]) - ord('a')] == 0:
                distinct_count -= 1
            left += 1
        count += right - left + 1
    return count
input_string = "abcabc"
k = 2
result = count_k_distinct_substrings(input_string, k)
print("Number of substrings with exactly", k, "distinct characters:", result)
