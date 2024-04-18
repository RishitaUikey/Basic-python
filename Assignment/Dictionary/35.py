'''Write a  Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]'''

from collections import Counter

data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
counter = Counter(data)
sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print(sorted_counter)
