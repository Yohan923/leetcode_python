"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.cur_min = None

    def push(self, x: int) -> None:
        self.cur_min = min(self.cur_min, x) if self.cur_min is not None else x
        self.stack.append((x, self.cur_min))

    def pop(self) -> None:
        self.stack.pop()
        self.cur_min = self.stack[len(self.stack) - 1][1] if len(self.stack) else None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0] if len(self.stack) else None

    def getMin(self) -> int:
        return self.cur_min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    s = MinStack()
    s.push(0)
    s.push(1)
    s.push(0)
    s.getMin()
    s.pop()
    s.getMin()
