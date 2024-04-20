'''Write a  Python program to get the powerset of a given iterable.
Sample Output:
Original list elements:
[1, 2]
Powerset of the said list:
[(), (1,), (2,), (1, 2)]
Original list elements:
[1, 2, 3, 4]
Powerset of the said list:
[(), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)]'''

def powerset(iterable):
    items = list(iterable)
    n = len(items)
    def generate_powerset(index):
        if index == n:
            yield ()
            return
        for subset in generate_powerset(index + 1):
            yield subset
            yield subset + (items[index],)
    return generate_powerset(0)

sample_iterables = [
    [1, 2],
    [1, 2, 3, 4]
]

for iterable in sample_iterables:
    print("Original list elements:")
    print(iterable)
    print("Powerset of the said list:")
    print(list(powerset(iterable)))

