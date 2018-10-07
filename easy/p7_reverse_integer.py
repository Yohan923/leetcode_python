"""Given a 32-bit signed integer, reverse digits of an integer."""


class Solution:
    # runtime 84ms
    def reverse(self, x):
        sign = (x > 0) - (x < 0)
        x *= sign
        rev = 0
        while x > 0:
            tmp = x % 10
            x = x // 10
            rev = rev * 10 + tmp
            if (2 ** 31) - 1 < rev or rev < -2 ** 31:
                return 0
        rev *= sign

        return rev

    # runtime 84ms
    def reverse_other(self, x):
        sign = (x > 0) - (x < 0)
        x *= sign
        tmp = str(x)
        x = int(tmp[::-1])
        return x * sign if -2 ** 31 < x < (2 ** 31) - 1 else 0
