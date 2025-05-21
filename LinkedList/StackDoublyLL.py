# Stack using Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class StackDoublyLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.prev = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.prev
        return data

    def peek(self):
        if not self.top:
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        elems = []
        current = self.top
        while current:
            elems.append(current.data)
            current = current.prev
        print("Stack (top to bottom):", elems)

# Example usage:
if __name__ == "__main__":
    stack = StackDoublyLL()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped:", stack.pop())
    stack.display()
    print("Top element:", stack.peek())

# Code by Harshit