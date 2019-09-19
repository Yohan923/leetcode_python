"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the
 largest product.
"""
from typing import List


class Solution:

    def max_product(self, nums: List[int]) -> int:

        if not nums:
            return -1

        cur_max = cur_min = fin_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            tmp = nums[i]
            cur_min = min(cur_min * tmp, tmp)
            cur_max = max(cur_max * tmp, tmp)
            fin_max = max(cur_max, fin_max)

        return fin_max

    """
    First, if there's no zero in the array, then the subarray with maximum product must start with the first 
    element or end with the last element. And therefore, the maximum product must be some prefix product or 
    suffix product. So in this solution, we compute the prefix product A and suffix product B, 
    and simply return the maximum of A and B.
    
    Why? Here's the proof:
    
    Say, we have a subarray A[i : j](i != 0, j != n) and the product of elements inside is P. Take P > 0 for 
    example: if A[i] > 0 or A[j] > 0, then obviously, we should extend this subarray to include A[i] or A[j]; 
    if both A[i] and A[j] are negative, then extending this subarray to include both A[i] and A[j] to get a 
    larger product. Repeating this procedure and eventually we will reach the beginning or the end of A.
    
    What if there are zeroes in the array? Well, we can split the array into several smaller ones. 
    That's to say, when the prefix product is 0, we start over and compute prefix profuct from the 
    current element instead. And this is exactly what A[i] *= (A[i - 1]) or 1 does.
    """

    # I don't understand this
    def max_product_1(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


if __name__ == '__main__':
    Solution().max_product([2, 3, -2, 4])
