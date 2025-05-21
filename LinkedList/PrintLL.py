# Pretty print Linked List in Python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def print_linked_list(head):
    while head:
        print(head.data, end=" -> " if head.next else "\n")
        head = head.next

# Example usage:
if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4))))
    print_linked_list(head)

# Code by Harshit