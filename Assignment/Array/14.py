'''Write a  Python program to find out if a given array of integers contains any duplicate elements. Return true if any value appears at least twice in the array, and return false if every element is distinct.
Sample Output:
False
True
True'''

def contains_duplicates(arr):
    seen = set()
    
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    
    return False

print(contains_duplicates([1, 2, 3, 4, 5]))  
print(contains_duplicates([1, 2, 3, 4, 1]))  
print(contains_duplicates([1, 1, 2, 2, 3]))  
