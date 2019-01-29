"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, preorder, inorder):
        def helper(preorder, inorder):
            if not inorder:
                return None

            tmp = preorder.popleft()
            node = TreeNode(tmp)

            i = inorder.index(tmp)

            node.left = helper(preorder, inorder[:i])
            node.right = helper(preorder, inorder[i + 1::])

            return node

        return helper(deque(preorder), inorder)
