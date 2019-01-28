"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root):
        if not root:
            return []

        ans = []
        level = [root]
        while len(level):
            tmp = []
            next_level = []

            for i in level:
                if i.left is not None:
                    next_level.append(i.left)
                if i.right is not None:
                    next_level.append(i.right)
                tmp.append(i.val)
            level = next_level
            ans.append(tmp)

        return ans

    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
