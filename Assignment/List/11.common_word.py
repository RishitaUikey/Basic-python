#  Write a Python function that takes two lists and returns True if they have at least one common member.

list1=(input("Enter the list: ")).split()
list2=(input("Enter the list: ")).split()
common=False

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

for i in list1:
    if i in list2:
        common=True
        break
if common==True:
    print("They have at least one common member.")
else:
    print("They do not have at least one common member.")
