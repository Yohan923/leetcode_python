"""Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    # worst case O(n)
    def search_range(self, nums, target):
        lo, hi = 0, len(nums) - 1
        start = end = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                start = end = mid
                break

        while start - 1 >= 0 and nums[start - 1] == target:
            start -= 1
        while end + 1 < len(nums) and nums[end + 1] == target:
            end += 1

        return [start, end]

    def search_range_other(self, nums, target):
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        lo, hi = 0, len(nums)
        start = end = -1

        while lo < hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
                start = hi

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
                end = lo - 1

        return [start, end]


def main():
    Solution().search_range_other([5,7,7,8,8,10], 8)


if __name__ == '__main__':
    main()
