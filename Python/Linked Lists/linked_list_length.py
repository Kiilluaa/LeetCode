# Given the head of a singly linked list, return the number of nodes it contains.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.val = next

def linked_list_length(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    return count