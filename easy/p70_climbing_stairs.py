"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution:

    # recursion too much for even 38 stairs
    def climb_stairs(self, n):

        if n == 0 or n == 1:
            return 1

        return Solution().climb_stairs(n - 1) + Solution().climb_stairs(n - 2)

    # fibonacci number solution
    def climb_stairs_fib(self, n):
        first = 0
        second = 1
        for i in range(n):
            third = first + second
            first = second
            second = third

        return second

def main():
    print(Solution().climb_stairs(38))


if __name__ == '__main__':
    main()
