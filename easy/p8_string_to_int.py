"""Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found.Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned."""


class Solution:

    # 64ms
    def my_atoi(self, str):
        result = 0
        sign = 1
        str = list(str.strip())
        if len(str) == 0:
            return 0

        if str[0] == '-' or str[0] == '+':
            sign = -1 if str[0] == '-' else 1
            str[0] = '0'

        if str[0].isdigit():
            for s in str:
                if s.isdigit():
                    result = result*10 + int(s)
                else:
                    break
            return result*sign if -2 ** 31 <= result <= (2 ** 31) - 1 else ((2**31)-(sign > 0))*sign

        return 0
