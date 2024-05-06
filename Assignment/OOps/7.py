# Write a Python program to create a class representing a linked list data structure. Include methods for 
# displaying linked list data, inserting and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)

print("Linked list data:")
llist.display()

llist.delete(3)

print("Linked list data after deleting node with value 3:")
llist.display()

