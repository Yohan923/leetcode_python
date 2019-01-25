"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution:
    def sort_colors(self, nums):

        white, red, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                tmp = nums[white]
                nums[white] = nums[red]
                nums[red] = tmp
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                tmp = nums[white]
                nums[white] = nums[blue]
                nums[blue] = tmp
                blue -= 1

    # lomuto partition?
    def sort_colors(self, nums):
        i = j = 0

        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
