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

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution(object):

    def spiral_order(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            # yields top row from [r1][c1] to [r1][c2]
            for c in range(c1, c2 + 1):
                yield r1, c
            # yields right col from [r1+1][c2] to [r2][c2]
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            # if one of them is same then there is only a single row or col therefore no bot or left
            if r1 < r2 and c1 < c2:
                # yields bot row from [r2][c2-1] to [r2][c1-1]
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                # yields left col from [r2][c1] to [r1-1][c1]
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return ans

    def spiral_order_draw(self, matrix):
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
