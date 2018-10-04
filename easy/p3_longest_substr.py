"""Given a string, find the length of the longest substring without repeating characters."""


class Solution:

    """difference in two pointers in the length of substring"""

    def length_of_longest_substring(self, s):
        buffer = dict()
        result = p = 0

        for x in range(len(s)):
            if s[x] in buffer and p <= buffer[s[x]]:
                p = buffer[s[x]] + 1
            else:
                result = max(result, x - p + 1)
            buffer[s[x]] = x

        return result


def main():
    x = Solution().length_of_longest_substring("pwwkew")

    "pklojp"


if __name__ == '__main__':
    main()
