"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from
 nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:

    # my simple solution
    def merge(self, nums1, m, nums2, n):
        nums1[m:m + n] = nums2
        nums1.sort()

    def merge_manual(self, nums1, m, nums2, n):
        rear_1, rear_2, rear_idx = m - 1, n - 1, m + n - 1

        while rear_1 >= 0 and rear_2 >= 0:
            if nums1[rear_1] < nums2[rear_2]:
                nums1[rear_idx] = nums2[rear_2]
                rear_2 -= 1
                rear_idx -= 1
            else:
                nums1[rear_idx] = nums1[rear_1]
                rear_1 -= 1
                rear_idx -= 1
        nums1[:rear_2 + 1] = nums2[:rear_2 + 1]

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
