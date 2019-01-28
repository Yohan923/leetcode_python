"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    def set_zeroes(self, matrix):
        is_col = False
        rl = len(matrix)
        cl = len(matrix[0])

        for i in range(rl):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, cl):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rl):
            for j in range(1, cl):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(cl):
                matrix[0][j] = 0

        if is_col:
            for i in range(rl):
                matrix[i][0] = 0
