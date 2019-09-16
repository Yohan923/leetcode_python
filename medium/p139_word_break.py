"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
 segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""


class Solution:
    def word_break(self, s, wordDict):
        if not s or not wordDict:
            return

        memo = [False for _ in range(len(s) + 1)]

        memo[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if memo[j] and (s[j:i] in wordDict):
                    memo[i] = True
                    break

        return memo[len(s)]
