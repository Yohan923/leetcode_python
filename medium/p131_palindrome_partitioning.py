"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]"""


class Solution:
    def partition(self, s):

        def is_palindrome(s):

            if not s:
                return False

            s_len = len(s)
            for i in range(s_len // 2):
                if s[i] != s[s_len - 1 - i]:
                    return False
            return True

        def dfs(s, cur_list, res_list):

            if s == "":
                res_list.append(cur_list.copy())
                return

            if len(s) <= 1:
                cur_list.append(s)
                res_list.append(cur_list.copy())
                cur_list.pop()
                return

            for i in range(len(s)):
                if is_palindrome(s[0:i + 1]):
                    cur_list.append(s[0:i + 1])
                    dfs(s[i + 1:], cur_list, res_list)
                    if len(cur_list) > 0:
                        cur_list.pop()

        cur_list = list()
        res_list = list()
        dfs(s, cur_list, res_list)

        return res_list


if __name__ == '__main__':
    Solution().partition("bb")
