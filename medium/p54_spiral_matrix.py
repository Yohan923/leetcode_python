"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

"""


class Solution:
    def spiral_order(self, matrix):
        if not matrix:
            return []

        rl, cl = len(matrix), len(matrix[0])

        seen = [[False] * cl for _ in matrix]
        ans = []

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        r = c = di = 0

        for _ in range(rl * cl):
            ans.append(matrix[r][c])
            seen[r][c] = True
            tmpr, tmpc = r + dr[di], c + dc[di]
            if 0 <= tmpr < rl and 0 <= tmpc < cl and not seen[tmpr][tmpc]:
                r = tmpr
                c = tmpc
            else:
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]

        return ans

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
