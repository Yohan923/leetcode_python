"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix):
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
