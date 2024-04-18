'''Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3'''

shop_items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
top_three = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)[:3]
for item, price in top_three:
    print(item, price)
