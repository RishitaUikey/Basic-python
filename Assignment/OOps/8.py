# Write a Python program to create a class representing a shopping cart. Include methods for adding and 
# removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def total_price(self):
        total = 0
        for item, quantity in self.items.items():
            total += quantity * item.price
        return total

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item1 = Item("Laptop", 3000)
item2 = Item("Mouse", 40)

cart = ShoppingCart()
cart.add_item(item1, item1.price, quantity=2)
cart.add_item(item2, item2.price)

print("Total price in the shopping cart:", cart.total_price())

cart.remove_item(item1)
print("Total price in the shopping cart after removing one laptop:", cart.total_price())
