# Write a Python program to implement insertion and deletion of circular queue.


class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.k == self.front

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full. Cannot enqueue element.")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = element
            print(f"Enqueued element: {element}")
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = element
            print(f"Enqueued element: {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
        elif self.front == self.rear:
            element = self.queue[self.front]
            self.queue[self.front] = None
            self.front = self.rear = -1
            print(f"Dequeued element: {element}")
            return element
        else:
            element = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.k
            print(f"Dequeued element: {element}")
            return element

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:")
            if self.front <= self.rear:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i])
            else:
                for i in range(self.front, self.k):
                    print(self.queue[i])
                for i in range(0, self.rear + 1):
                    print(self.queue[i])


# Create a circular queue instance with size 5
cq = CircularQueue(5)

# Enqueue elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # Attempt to enqueue when the queue is full

# Display the queue
cq.display()

# Dequeue elements
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()  # Attempt to dequeue when the queue is empty

# Display the queue after dequeue
cq.display()
