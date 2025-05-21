# Queue using Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class QueueDoublyLL:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return not self.front

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def display(self):
        res, curr = [], self.front
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

if __name__ == "__main__":
    q = QueueDoublyLL()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue:", q.display())
    print("Dequeued:", q.dequeue())
    print("Queue after dequeue:", q.display())
    print("Front element:", q.peek())

# Code by Harshit