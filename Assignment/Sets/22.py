#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

def pairs_sum(l, target_sum):
    pairs = set()  
    seen = set()   
    
    for num in l:
        complement = target_sum - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)
    
    return pairs


l = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7

pairs = pairs_sum(l, target_sum)

print("Pairs with sum", target_sum, "are:")
for pair in pairs:
    print(pair)
