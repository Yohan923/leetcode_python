"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        rot = lo
        lo = 0
        hi = len(nums) - 1
        # The usual binary search and accounting for rotation.
        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (mid + rot) % len(nums)
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


def main():
    Solution().search([5, 1, 2, 3, 4], 1)


if __name__ == '__main__':
    main()
