"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""


class Solution:
    def num_decodings(self, s):
        mem = [i * 0 for i in range(len(s) + 1)]

        mem[0] = 1
        mem[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            st = int(s[i - 1:i])
            nd = int(s[i - 2:i])

            mem[i] += mem[i - 1] if 1 <= st <= 9 else 0
            mem[i] += mem[i - 2] if 10 <= nd <= 26 else 0

        return mem[len(s)]

    """
    :type s: str
    :rtype: int
    """


if __name__ == '__main__':
    Solution().num_decodings("12")
