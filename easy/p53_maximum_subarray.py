"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

"""


class Solution:
    """
    this problem was discussed by Jon Bentley (Sep. 1984 Vol. 27 No. 9 Communications of the ACM P885)

    the paragraph below was copied from his paper (with a little modifications)

    algorithm that operates on arrays: it starts at the left end (element A[1]) and scans through to the right end (
    element A[n]), keeping track of the maximum sum subvector seen so far. The maximum is initially A[0]. Suppose
    we've solved the problem for A[1 .. i - 1]; how can we extend that to A[1 .. i]? The maximum sum in the first I
    elements is either the maximum sum in the first i - 1 elements (which we'll call MaxSoFar), or it is that of a
    subvector that ends in position i (which we'll call MaxEndingHere).

    MaxEndingHere is either A[i] plus the previous MaxEndingHere, or just A[i], whichever is larger.
    """

    def max_sub_array(self, nums):
        max = maxEnd = nums[0]

        for i in range(1, len(nums)):
            maxEnd = nums[i] + maxEnd if nums[i] + maxEnd > nums[i] else nums[i]
            max = max if max > maxEnd else maxEnd

        return max


def main():
    print(Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    main()
