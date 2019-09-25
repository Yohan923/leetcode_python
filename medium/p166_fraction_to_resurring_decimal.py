"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.
"""


class Solution:
    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        n, rem = divmod(numerator, denominator)
        result = [sign + str(n), "."]
        memo = dict()
        idx = 0

        while rem not in memo:
            memo[rem] = idx
            n, rem = divmod(rem * 10, denominator)
            result.append(str(n))
            idx += 1

        idx = memo.get(rem)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
