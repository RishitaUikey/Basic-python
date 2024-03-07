# Write a Python script to sort (ascending and descending) a dictionary by value.

x={'a':9,'b':15,'c':4,'d':19,'e':28,'f':12}
ascending=dict(sorted(x.items(),key=lambda item: item[1]))
decending=dict(sorted(x.items(),key=lambda item: item[1] ,reverse=True))
print("Sorted a dictionary by value in ascending:",ascending)
print("Sorted a dictionary by value in decending:",decending)
















