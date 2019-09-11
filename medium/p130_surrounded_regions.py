"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two
cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def change_connected(i, j, dims):
            for (k, l) in [(max(i - 1, 0), j), (i, max(j - 1, 0)), (i, min(j + 1, dims[1] - 1)),
                           (min(i + 1, dims[0] - 1), j)]:
                if board[k][l] == "O":
                    board[k][l] = "1"
                    change_connected(k, l, dims)

        if not board:
            return

        dims = (len(board), len(board[0]))

        for i in [0, dims[0] - 1]:
            for j in range(dims[1]):
                if board[i][j] == "O":
                    board[i][j] = "1"
                    change_connected(i, j, dims)

        for j in [0, dims[1] - 1]:
            for i in range(1, dims[0] - 1):
                if board[i][j] == "O":
                    board[i][j] = "1"
                    change_connected(i, j, dims)

        for i in range(dims[0]):
            for j in range(dims[1]):
                if board[i][j] == "1":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


if __name__ == '__main__':
    Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
