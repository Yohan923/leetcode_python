"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map
to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


# 32 ms beats 100% apparently lol
class Solution:
    def letter_combinations(self, digits):
        d = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}

        l = list()
        for i in digits:
            l.append(d[i])
        result = Solution().find(l)

        return result

    def find(self, lists):
        l = len(lists)
        if l == 1:
            return lists[0]
        elif l == 0:
            return []
        elif l == 2:
            result = list()
            for i in lists[0]:
                for j in lists[1]:
                    result.append(i + j)
            return result
        else:
            return Solution().find([Solution().find(lists[0:l // 2]), Solution().find(lists[l // 2:l])])


def main():
    print(Solution().letter_combinations("23"))


if __name__ == '__main__':
    main()
