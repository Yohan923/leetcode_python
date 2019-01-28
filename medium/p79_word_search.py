"""
Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


def can_find(board, word, i, j):
    if len(word) <= 0:
        return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    else:
        tmp = board[i][j]
        board[i][j] = "#"
        result = can_find(board, word[1:], i + 1, j) or \
                 can_find(board, word[1:], i - 1, j) or \
                 can_find(board, word[1:], i, j + 1) or \
                 can_find(board, word[1:], i, j - 1)
        board[i][j] = tmp
        return result


class Solution:
    def exist(self, board, word):
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if can_find(board, word, i, j):
                    return True

        return False


def main():
    Solution().exist([["a", "a"]], "aaa")


if __name__ == '__main__':
    main()

    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
