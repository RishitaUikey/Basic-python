'''Write a  Python program to find the minimum window in a given string that will contain all the characters of another given string.
Example 1
Input : str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output: Minimum window is "OERIUS"'''

from collections import Counter

def min_window(str1, str2):
    target_counts = Counter(str2)
    target_len = len(str2)
    min_window_size = float('inf')
    min_window = ""

    left = 0
    right = 0
    window_counts = Counter()

    while right < len(str1):
        window_counts[str1[right]] += 1

        if window_contains_target(window_counts, target_counts):
            while window_contains_target(window_counts, target_counts):
                window_size = right - left + 1
                if window_size < min_window_size:
                    min_window_size = window_size
                    min_window = str1[left:right + 1]

                window_counts[str1[left]] -= 1
                left += 1

        right += 1

    return min_window

def window_contains_target(window_counts, target_counts):
    for char, count in target_counts.items():
        if window_counts[char] < count:
            return False
    return True

str1 = "PRWSOERIUSFK"
str2 = "OSU"
result = min_window(str1, str2)
print("Minimum window is:", result)
