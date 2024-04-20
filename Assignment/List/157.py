'''Write a  Python program to interleave lists of varying lengths.
Original lists:
[2, 4, 7, 0, 5, 8]
[2, 5, 8]
[0, 1]
[3, 3, -1, 7]
Interleave said lists of different lengths:
[2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]'''

def interleave_lists(*lists):
    max_length = max(map(len, lists)) 
    interleaved = []
    for i in range(max_length):
        for lst in lists:
            if i < len(lst):
                interleaved.append(lst[i])
    return interleaved

original_lists = [
    [2, 4, 7, 0, 5, 8],
    [2, 5, 8],
    [0, 1],
    [3, 3, -1, 7]
]
print("Interleave said lists of different lengths:")
print(interleave_lists(*original_lists))
