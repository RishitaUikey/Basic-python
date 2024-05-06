''' Write a  Python program to compute the element-wise sum of given tuples.
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)'''

t = ((1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1))
element_wise_sum = tuple(sum(values) for values in zip(*t))
for t in t:
    print(t)
print("Element-wise sum of the said tuples:")
print(element_wise_sum)
