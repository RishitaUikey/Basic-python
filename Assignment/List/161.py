'''Write a  Python program to check if a given list increases strictly. Moreover, if removing only one element from the list results in a strictly increasing list, we still consider the list true.
True
True
True
True
True
True
True
True
True
True
True
False
False
False
False
False'''

def is_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

def is_strictly_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            if i > 0 and lst[i - 1] < lst[i + 1]:
                continue
            elif i < len(lst) - 2 and lst[i] < lst[i + 2]:
                continue
            else:
                return False
    return True

def check_strict_increase(lst):
    result = []
    for i in range(len(lst)):
        sub_lst = lst[:i] + lst[i+1:]
        result.append(is_increasing(sub_lst))
    return result

test_lists = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 5, 5],
    [1, 2, 3, 5, 6],
    [1, 2, 3, 6, 5],
    [1, 3, 3, 4, 5],
    [1, 2, 4, 3, 5],
    [1, 2, 3, 5, 4],
    [1, 2, 3, 4, 3],
    [1, 2, 3, 2, 5],
    [1, 2, 3, 6, 4],
    [1, 2, 3, 5, 3],
    [5, 4, 3, 2, 1],
    [1, 2, 2, 2, 5],
    [1, 2, 2, 5, 5],
    [1, 1, 1, 1, 1]
]

for lst in test_lists:
    print(is_strictly_increasing(lst))
