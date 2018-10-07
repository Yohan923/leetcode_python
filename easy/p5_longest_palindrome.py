"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000."""


def is_palindrome(s):
    length = len(s) - 1
    start = 0
    while start < length:
        if s[start] != s[length]:
            return False
        start += 1
        length -= 1
    return True

def expand_palindrome(s, r, l):
    while l >=0 and r < len(s) and s[l] == s[r]:
        r += 1
        l -=1

    return r - l - 1


class Solution:
    """brute force solution O(n3) failed to submit"""
    def longest_palindrome(self, s):
        result = len(s)
        while result > 0:
            start = 0
            end = result
            while end <= len(s):
                if is_palindrome(s[start:end]):
                    return s[start:end]
                start += 1
                end += 1
            result -= 1

        return ""

    """"""
    def longest_palindrome_other(self, s):
        start = finish = 0
        for x in range(len(s)):
            len0 = expand_palindrome(s, x, x)
            len1 = expand_palindrome(s, x+1, x)
            max_len = max(len0, len1)
            if max_len > finish - start:
                start = x - (max_len - 1)//2
                finish = x + max_len//2
        return s[start:finish+1]


def main():
    print(Solution().longest_palindrome_other("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))


if __name__ == '__main__':
    main()
