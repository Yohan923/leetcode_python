"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique

 triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets."""


class Solution:

    # exceeded time limit
    def three_sum(self, nums):
        d = dict()
        s = list()
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    indx = d.get(0 - nums[i] - nums[j], None)
                    if indx is not None and indx != i and indx != j:
                        if self.is_unique(s, [nums[i], nums[j], nums[indx]]):
                            s.append([nums[i], nums[j], nums[indx]])

        return s

    def is_unique(self, s, lis):
        lis.sort()
        for i in s:
            i.sort()
            if i == lis:
                return False
        return True

    # 1416 ms sort list and find pairs by two way search
    def three_sum_other(self, nums):
        result = list()
        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                a = 0 - nums[lo] - nums[hi]
                if a == nums[i]:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif a < nums[i]:
                    hi -= 1
                else:
                    lo += 1

        return result


def main():
    a = Solution().three_sum_other([1,-1,-1,0])
    print(a)


if __name__ == '__main__':
    main()
