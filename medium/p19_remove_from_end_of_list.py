"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 36ms
    def remove_nth_from_end(self, head, n):
        h = head
        l = list()

        while head:
            l.append(head)
            head = head.next

        if len(l) != n:
            node = l[len(l) - n - 1]
            node.next = node.next.next
        else:
            return h.next
        return h

    # uses no extra memory
    def remove_nth_from_end_other(self, head, n):

        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
