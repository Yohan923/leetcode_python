"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
of the first two lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_lists(self, l1, l2):
        new_head = tmp = ListNode(0)

        while l1 is not None or l2 is not None:
            if l1 is None:
                tmp.next = l2
                l2 = None
            elif l2 is None:
                tmp.next = l1
                l1 = None
            elif l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        return new_head.next
