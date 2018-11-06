"""
Given a collection of distinct integers, return all possible permutations.

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        permutes = self.permute(nums[1: len(nums)])
        result = list()
        for i in permutes:
            for j in range(len(i)):
                tmp = list(i)
                tmp.insert(j, nums[0])
                result.append(tmp)
            tmp = list(i)
            tmp.append(nums[0])
            result.append(tmp)
        return result

def main():
    Solution().permute([1,2,3])
if __name__ == '__main__':
    main()

