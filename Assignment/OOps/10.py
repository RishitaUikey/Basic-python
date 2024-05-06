# Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty.")
            return None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued item from the queue:", queue.dequeue())
print("Dequeued item from the queue:", queue.dequeue())
