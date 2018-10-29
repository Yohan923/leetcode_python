"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    # brute force: 48ms
    def generate_parenthesis(self, n):
        if n == 0:
            return ""
        result = list()
        self.gen_parenthesis(n, 0, "", result)

        return result

    def gen_parenthesis(self, open, close, str, result):
        if open == 0 and close == 0:
            result.append(str)

        if open > 0:
            self.gen_parenthesis(open - 1, close + 1, str + "(", result)
        if close > 0:
            self.gen_parenthesis(open, close - 1, str + ")", result)

    # closure number
    def generate_parenthesis_other(self, n):
        if n == 0:
            return [""]

        result = list()
        for c in range(n):
            for left in self.generate_parenthesis_other(c):
                for right in self.generate_parenthesis_other(n - 1 - c):
                    result.append("({}){}".format(left, right))
        return result


def main():
    Solution().generate_parenthesis_other(3)


if __name__ == '__main__':
    main()
