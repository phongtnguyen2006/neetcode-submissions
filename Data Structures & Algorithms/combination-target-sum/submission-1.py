class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        curr = []

        def dfs(i, total):
            if total == target:
                sol.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, total + nums[i])
            curr.pop()

            dfs(i + 1, total)


        dfs(0, 0)

        return sol
