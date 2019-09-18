"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't
be any divide by zero operation.
"""
from math import ceil, floor
from typing import List


class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:
        if not tokens:
            return -1

        stack = list()
        ops = ["+", "*", "-", "/"]

        for token in tokens:
            if token in ops:
                exp1 = int(stack.pop())
                exp2 = int(stack.pop())
                result = 0

                if token == "+":
                    result = exp2 + exp1
                elif token == "-":
                    result = exp2 - exp1
                elif token == "*":
                    result = exp2 * exp1
                else:
                    result = int(exp2 / exp1)

                stack.append(result)
            else:
                stack.append(token)

        return stack.pop()


if __name__ == '__main__':
    Solution().eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
