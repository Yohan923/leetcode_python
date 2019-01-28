"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzag_level_order(self, root):
        if not root:
            return []

        ans = []
        level = [root]

        di = 1

        while len(level):
            di = 0 if di else 1
            tmp = []
            next_level = []

            for i in level:
                if i.left is not None:
                    next_level.append(i.left)
                if i.right is not None:
                    next_level.append(i.right)
                tmp.append(i.val)

            level = next_level
            if di:
                tmp.reverse()
            ans.append(tmp)

        return ans
