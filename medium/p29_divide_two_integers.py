"""

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers. The divisor will never be 0. Assume we are dealing with an
environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
of this problem, assume that your function returns 231 − 1 when the division result overflows.

"""


class Solution:
    # exceeds time limit
    def divide(self, dividend, divisor):
        flags = [True, True]
        if dividend < 0:
            flags[0] = False
            dividend = dividend - dividend - dividend
        if divisor < 0:
            flags[1] = False
            divisor = divisor - divisor - divisor
        result = 0
        if divisor == 1:
            result = dividend
        else:
            while dividend >= divisor:
                result += 1
                dividend = dividend - divisor
        if flags[0] != flags[1]:
            result = result - result - result

        return (2 ** 31 - 1) if result > 2 ** 31 - 1 or result < -(2 ** 31) else result

    def divide_other(self, dividend, divisor):
        if divisor == 0 or (dividend <= -(2 ** 31) and divisor == -1):
            return 2 ** 31 - 1

        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            tmp = divisor
            mult = 1
            while dividend >= tmp << 1:
                tmp <<= 1
                mult <<= 1
            dividend -= tmp
            result += mult

        return result if sign == 1 else -result

def main():

    print(Solution().divide_other(7, -3))

if __name__ == '__main__':
    main()
