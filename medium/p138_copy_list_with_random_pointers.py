"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null.

Return a deep copy of the list.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head):

        if not head:
            return

        iterator = head
        # make a copy of each node and attach it to the original node's next
        while iterator:
            tmp = Node(iterator.val, iterator.next, None)
            iterator.next = tmp
            iterator = iterator.next.next

        iterator = head
        # assign random for each of the copy node
        while iterator:
            if iterator.random:
                iterator.next.random = iterator.random.next
            iterator = iterator.next.next

        iterator = head
        tmp_head = Node(0, None, None)
        result = tmp_head
        # extract copy nodes and restore original
        while iterator:
            tmp = iterator.next
            iterator.next = tmp.next

            tmp_head.next = tmp
            tmp_head = tmp_head.next

            iterator = iterator.next

        return result.next

    def copy_random_list_2(self, head):

        if not head:
            return

        nodes = dict()

        iterator = head

        while iterator:
            nodes[iterator] = Node(iterator.val, None, None)
            iterator = iterator.next

        iterator = head

        while iterator:
            if iterator.next:
                nodes[iterator].next = nodes[iterator.next]
            if iterator.random:
                nodes[iterator].random = nodes[iterator.random]
            iterator = iterator.next

        return nodes[head]
