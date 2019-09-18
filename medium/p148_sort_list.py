"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sort_list(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        # dummy node always points to head since prev always start from dummy so
        # every sublist will be sorted attaching to prev/dummy.
        dummy = ListNode(0)
        dummy.next = head

        sublists = list([0, 0])
        done = False
        step = 1
        # do following for doubling step sizes
        while not done:
            done = True
            prev = dummy
            # the remaining nodes that has not been merged
            remaining = dummy.next

            # divide into sublist of step size and merge while there are still nodes remainning
            while remaining:
                # allocate nodes for two sub lists
                for i in range(0, 2):
                    sublists[i] = remaining
                    tail = ListNode(None)

                    # one sub list step number of nodes.
                    for j in range(0, step):
                        if not remaining:
                            break
                        tail = remaining
                        # move remaining forward, until step size has reached or no more remaining
                        remaining = remaining.next

                    # sublist nodes has been allocated, terminate the sublist
                    if tail:
                        tail.next = None

                # finished when it is the first iteration of this "step" pass and
                # the two sub lists are of the entire original list, thus remaining is None
                done &= (not remaining)

                # if 2 sublist are present
                if sublists[1]:
                    # merge the two sub lists attaching to prev, which always starts at dummy
                    # on first iteration of one pass meaning dummy always point to head of list.
                    while sublists[0] or sublists[1]:
                        i = 0 if not sublists[1] or sublists[0] and sublists[0].val <= sublists[1].val else 1
                        prev.next = sublists[i]
                        sublists[i] = sublists[i].next
                        prev = prev.next
                    # terminate prev
                    prev.next = None
                else:
                    prev.next = sublists[0]

            step *= 2

        return dummy.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    Solution().sort_list(head)
