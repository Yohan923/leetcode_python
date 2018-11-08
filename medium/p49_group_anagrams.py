"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def group_anagrams(self, strs):
        result = dict()

        for i in strs:
            tmp = list(i)
            tmp.sort()
            tmp = "".join(tmp)
            if result.get(tmp):
                result.get(tmp).append(i)
            else:
                result[tmp] = [i]
        r = list()
        for i in result.items():
            r.append(i[1])

        return r
def main():

    print(Solution().group_anagrams(["eat","tea","tan","ate","nat","bat"]))
if __name__ == '__main__':
    main()
