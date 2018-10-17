"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z."""


class Solution:

    # 52ms
    def longest_common_prefix(self, strs):
        l = len(strs)
        if l == 1:
            return strs[0]
        elif l == 0:
            return ""

        lcpl = Solution().longest_common_prefix(strs[0:l // 2])
        lcpr = Solution().longest_common_prefix(strs[l // 2:l])

        prefix = ""
        x = 0
        while x < len(lcpl) and x < len(lcpr):
            if lcpl[x] == lcpr[x]:
                prefix += lcpr[x]
            else:
                break
            x += 1
        return prefix

    # try binary search approach and vertical scanning