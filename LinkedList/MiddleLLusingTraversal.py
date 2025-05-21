# Find middle of a linked list using one traversal
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("Middle element:", find_middle(head))

# Code by Harshit