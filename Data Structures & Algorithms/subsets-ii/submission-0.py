class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        self.curr = []
        nums.sort()
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, i):
        if i == len(nums):
            return

        # include nums[i]
        self.curr.append(nums[i])
        self.res.append(self.curr.copy())
        self.backtrack(nums, i + 1)
        self.curr.pop()

        # exclude nums[i] — skip past all its duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.backtrack(nums, i + 1)