# Reverse Stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def __repr__(self):
        return repr(self.items)

def reverse_stack(stack):
    temp = []
    while not stack.is_empty():
        temp.append(stack.pop())
    for item in temp:
        stack.push(item)

if __name__ == "__main__":
    stack = Stack()
    for i in [1, 2, 3, 4, 5]:
        stack.push(i)
    print("Original Stack:", stack)
    reverse_stack(stack)
    print("Reversed Stack:", stack)

# Code by Harshit