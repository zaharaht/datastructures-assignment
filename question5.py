#Write an algorithm to insert an element into Circular Queue.
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity # maximum number the queue can have 
        self.storage = [None] * capacity # allocating memory for maximum number of items that can be in the queue
        self.size = 0 # number of items currently in the queue
        self.front = 0
        self.rear = 0
        
    def isFull(self):
        if(self.capacity == self.size):
            return True
        
    def enqueue(self, item):
        if (self.isFull()):
            raise Exception(f"The queue of capacity {self.capacity} is full: {self.storage}")
        self.storage[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity # calculating the position of the tail 
        self.size +=1
        print(f"Current elements in queue: {self.storage}")
            
cq = CircularQueue(4)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(6)
#cq.enqueue(12) # will raise an exception