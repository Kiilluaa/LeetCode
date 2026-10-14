class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sum_linked_list(head):
    total = 0
    current = head
    while current is not None:
        total += current.val
        current = current.next
    return total

# Test 1: Three nodes
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)

print(sum_linked_list(head))  # Expected: 60

# Test 2: Single node
head = ListNode(7)

print(sum_linked_list(head))  # Expected: 7

# Test 3: Empty linked list
head = None

print(sum_linked_list(head))  # Expected: 0

# Test 4: Negative values
head = ListNode(-5)
head.next = ListNode(10)
head.next.next = ListNode(-3)

print(sum_linked_list(head))  # Expected: 2