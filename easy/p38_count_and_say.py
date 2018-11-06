"""

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""


class Solution:
    def count_and_say(self, n):
        seq = list()
        seq.append("1")

        for _ in range(n-1):
            seq.append(self.say(seq[len(seq) - 1]))

        return seq.pop()

    def say(self, s):
        result = ""
        no = 0
        val = 0
        for i in s:
            if val == 0:
                val = int(i)
                no += 1
                continue
            if val != int(i):
                result = result + str(no) + str(val)
                val = int(i)
                no = 0
                no += 1
            elif val == int(i):
                no += 1
        result = result + str(no) + str(val)
        return result

def main():
    print(Solution().count_and_say(4))


if __name__ == '__main__':
    main()