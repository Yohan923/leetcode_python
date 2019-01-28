"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root):

        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)

        return helper(root, root)

    def is_symmetric_iter(self, root):
        q = [root, root]

        while len(q) > 0:
            node1 = q.pop()
            node2 = q.pop()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            q.insert(0, node1.left)
            q.insert(0, node2.right)
            q.insert(0, node1.right)
            q.insert(0, node2.left)

        return True

    """
    :type root: TreeNode
    :rtype: bool
    """
