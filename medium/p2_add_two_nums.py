"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse 
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def add_two_numbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        result = head
        while l1 is not None or l2 is not None or carry != 0:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            sums = a + b + carry

            if sums < 10:
                carry = 0
                result.next = ListNode(sums)
            else:
                carry = 1
                result.next = ListNode(sums - 10)

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            result = result.next

        return head.next

    # concise but slower from submission
    def add_two_numbers_other(self, l1, l2):
        carry = 0
        head = ListNode(0)
        result = head
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            result.next = ListNode(carry % 10)
            carry = carry // 10
            result = result.next

        return head.next
