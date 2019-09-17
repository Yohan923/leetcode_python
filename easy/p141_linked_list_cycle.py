"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head):

        if not head:
            return

        memo = dict()

        while head:
            if memo.get(head):
                return True
            memo[head] = 1
            head = head.next

        return False

    def has_cycle_2(self, head):

        if not head:
            return

        slow = head
        fast = head

        while True:
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

