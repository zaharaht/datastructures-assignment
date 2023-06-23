# Write a python program to implement Enqueue and Dequeue operation
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        added = self.queue[-1]
        print(
            f"{added} has been added to the queue. Current elements in queue; {self.queue}")
        
    def dequeue(self):
        if len(self.queue) == 0:
            print(f"Sorry, the queue is empty.")
        else:
            removed = self.queue.pop(0)
            print(f"The last element {removed} has been removed from the queue. Current elements in queue; {self.queue}")
            
one = Queue()
# one.enqueue(1)
# one.enqueue(2)
# one.dequeue()