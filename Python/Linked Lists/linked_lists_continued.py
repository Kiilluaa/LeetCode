# Given the head of a linked list and a target value, remove the first occurrence of that target and return the updated head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_value(head, target):
    if head is None:
        return None

    if head.val == target:
        return head.next
    
    current = head
    while current is not None:
        if current.next is not None and current.next.val == target:
            current.next = current.next.next
            return head
        else:
            current = current.next
    return head

def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True
    return False

def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    for fast in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

def get_intersection_node(headA, headB):
    p1 = headA
    p2 = headB

    while p1 is not p2:
        if p1:
            p1 = p1.next
        else:
            p1 = headB
        if p2:
            p2 = p2.next
        else:
            p2 = headA
    return p1
        


def to_list(head):
    result = []
    current = head

    while current is not None:
        result.append(current.val)
        current = current.next

    return result

