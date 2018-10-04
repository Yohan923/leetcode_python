"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""


class Solution(object):

    def two_sums(self, nums, target):
        for x in range(0, len(nums)):
            dif = target - nums[x]
            if dif in nums:
                y = nums.index(dif)
                if x != y:
                    return [x, y]

    def two_sums_other(self, nums, target):
        m = dict()

        for x in range(0, len(nums)):
            if m.get(nums[x]) is not None:
                return [m.get(nums[x]), x]
            else:
                m[target - nums[x]] = x

        return [0, 0]


