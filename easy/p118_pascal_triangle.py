"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        if not numRows:
            return []

        ans = []

        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if not j or j == i:
                    row.append(1)
                else:
                    tmp = ans[len(ans) - 1]
                    row.append(tmp[j - 1] + tmp[j])
            ans.append(row)

        return ans
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
