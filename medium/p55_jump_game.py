"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

"""
GOOD = True


class Solution:
    # time limit
    # DP bottom up
    def can_jump(self, nums):
        nums[len(nums) - 1] = GOOD
        for i in range(len(nums) - 2, -1, -1):
            max_length = min(i + nums[i] + 1, len(nums))
            for j in range(i + 1, max_length):
                if nums[j] is GOOD:
                    nums[i] = GOOD
                    break

        return nums[0] is GOOD

    # only ever reach the right most GOOD anyways from bottom up method
    def can_jump_greedy(self, nums):
        cur_good = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if cur_good <= i + nums[i]:
                cur_good = i

        return cur_good == 0


"""
:type nums: List[int]
:rtype: bool
"""
