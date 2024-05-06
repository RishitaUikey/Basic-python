'''Write a  Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
Note: Use dictionaries and lists to store the data.'''

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, table_number, order):
        self.customer_orders.append((table_number, order))

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("Table Reservations:")
        print(", ".join(map(str, self.booked_tables)))

    def print_customer_orders(self):
        print("Customer Orders:")
        for table_number, order in self.customer_orders:
            print(f"Table {table_number}: {order}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Pizza", 10)
restaurant.add_item_to_menu("Burger", 8)
restaurant.add_item_to_menu("Salad", 6)

restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(3)

restaurant.customer_order(1, "Pizza, Salad")
restaurant.customer_order(2, "Burger")
restaurant.customer_order(3, "Pizza, Burger, Salad")

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
