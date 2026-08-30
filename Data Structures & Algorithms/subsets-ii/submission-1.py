class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """

        [1, 2, 2, 1] -> [1, 1, 2, 2]
        

        """

        nums.sort()
        sol = []
        curr = []
        def dfs(i):
            if i > len(nums) - 1:
                sol.append(curr[:])
                return 

            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return sol

