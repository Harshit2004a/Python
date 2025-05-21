# Search an Element in a Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        temp = self.head
        if not temp:
            return False
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False


cll = CircularLinkedList()
for val in [10, 20, 30]:
    cll.append(val)
print(cll.search(20))  # True
print(cll.search(40))  # False

# Code by Harshit