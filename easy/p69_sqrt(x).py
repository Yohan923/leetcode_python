"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is
returned.

"""


class Solution:

    # simplified newtons method
    def my_sqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r

    # binary search method
    def my_sqrt_bs(self, x):

        if x == 0:
            return 0

        lo = 1
        hi = x

        while True:
            mid = lo + (hi - lo)//2

            if mid > x//mid:
                hi = mid - 1
            elif (mid + 1) > x//(mid + 1):
                return mid
            else:
                lo = mid + 1

def main():
    Solution().my_sqrt_bs(4)

if __name__ == '__main__':
    main()