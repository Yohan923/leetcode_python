"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # iterative
    def inorder_traversal(self, root):
        cur = root
        ans = []
        stack = []

        while cur is not None or len(stack) != 0:

            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans

    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def inorder_traversal_recur(self, root):
        ans = []
        Solution().helper(root, ans)
        return ans

    def helper(self, node, ans):
        if node is None:
            return

        Solution().helper(node.left, ans)
        ans.append(node.val)
        Solution().helper(node.right, ans)
