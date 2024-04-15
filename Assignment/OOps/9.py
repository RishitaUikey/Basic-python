# Write a Python program to create a class representing a stack data structure. Include methods for pushing,
# popping and displaying elements.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty.")
            return None

    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty.")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

popped_item = stack.pop()
print("Popped item from the stack:", popped_item)

stack.display()
