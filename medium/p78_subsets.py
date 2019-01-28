"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):

        if not nums:
            return [[]]

        subs = Solution().subsets([i for i in nums[0:len(nums) - 1]])
        ans = []

        for i in subs:
            ans.append(i)
            tmp = list(i)
            tmp.append(nums[len(nums) - 1])
            ans.append(tmp)
        return ans

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


def main():
    Solution().subsets([1, 2, 3])


if __name__ == '__main__':
    main()
