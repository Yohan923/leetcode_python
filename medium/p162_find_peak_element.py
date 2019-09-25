"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Your solution should be in logarithmic complexity.
"""
from typing import List


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        hi = len(nums) - 1
        lo = 0

        while hi > lo:
            mid = (hi + lo) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1

        return lo
