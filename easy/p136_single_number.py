"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    def single_number(self, nums):
        d = dict()

        for num in nums:
            if d.pop(num, 1):
                d[num] = 0

        return d.popitem()

    # math approach
    # 2∗(a+b+c)−(a+a+b+b+c)=c

    def single_number_2(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    # XOR approach

    def single_number_3(self, nums):
        tmp = 0

        for num in nums:
            tmp ^= num

        return tmp
