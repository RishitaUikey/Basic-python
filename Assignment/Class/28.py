'''Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price.'''

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }
        print(f"Item {item_id} added to inventory.")

    def update_item(self, item_id, stock_count=None, price=None):
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
            print(f"Item {item_id} updated.")
        else:
            print(f"Item {item_id} not found in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.items:
            item_details = self.items[item_id]
            print(f"Item ID: {item_id}")
            for key, value in item_details.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print(f"Item {item_id} not found in inventory.")

inventory = Inventory()
inventory.add_item("1001", "Laptop", 10, 800)
inventory.add_item("1002", "Smartphone", 20, 500)
inventory.update_item("1001", stock_count=8)
inventory.update_item("1002", price=550)

inventory.check_item_details("1001")
inventory.check_item_details("1002")
inventory.check_item_details("1003")  
