## Runner Techniques

This is when you iterate through the Linked list with two pointers simultaneously, one ahead of the order. We can use this to solve find mid of a linked list, end of linked list, or determine if there is a cycle in the linked list. 

# Recursion

We can solve linked list problems with Recursion, These take at O(n) space. Recursion is when a function calls itself. 

For example we can reverse a linked list using recursion

```
class Node:
def __init__(self, val):
    self.data = val
    self.next = None

def reverse_list(head):
    if head is None or head.next is None:
        return head
    
    rev_head = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return rev_head