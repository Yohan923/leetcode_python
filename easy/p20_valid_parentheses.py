"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def is_valid(self, s):
        if s != "":
            result = False
            queue = list()
            for i in s:
                if i == "{":
                    result = True
                    queue.append("}")
                elif i == "(":
                    result = True
                    queue.append(")")
                elif i == "[":
                    result = True
                    queue.append("]")
                elif i == "}" or i == ")" or i == "]":
                    if len(queue) != 0 and queue[len(queue) - 1] == i:
                        queue.pop()
                    else:
                        return False
            if len(queue) != 0:
                return False
            else:
                return result
        else:
            return True
