"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root):
        def helper(node):
            if not node:
                return 0

            return max(helper(node.left), helper(node.right)) + 1

        if not root:
            return 0

        return max(helper(root.right), helper(root.left)) + 1

    """
    :type root: TreeNode
    :rtype: int
    """
