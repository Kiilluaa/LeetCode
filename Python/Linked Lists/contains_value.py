# Given the head of a singly linked list and an integer target, return True if 
# the target exists in the linked list. Otherwise, return False.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def contains_value(head, target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)

print(contains_value(head, 20))  # Expected: True
print(contains_value(head, 10))  # Expected: True
print(contains_value(head, 30))  # Expected: True
print(contains_value(head, 40))  # Expected: False

print(contains_value(None, 5))   # Expected: False

single = ListNode(7)
print(contains_value(single, 7))  # Expected: True
print(contains_value(single, 3))  # Expected: False