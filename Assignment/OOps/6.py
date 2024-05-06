# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top element of the stack:", stack.peek())

popped_item = stack.pop()
print("Popped item from the stack:", popped_item)
print("Stack size after popping:", stack.size())
