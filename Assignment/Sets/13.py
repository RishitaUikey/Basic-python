# Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.

s = {1, 2, 3, 4, 5}
frozen = frozenset(s)

try:
    frozen.add(6)
except AttributeError as e:
    print("Error:", e)

print("Regular set:", s)
print("Frozen set:", frozen)
