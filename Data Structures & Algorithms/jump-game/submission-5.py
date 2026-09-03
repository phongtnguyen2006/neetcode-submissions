class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True
        
        for i in range(len(nums) - 2, - 1, -1):
            print(nums[i])
            for j in range(0, nums[i] + 1):
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
        print(dp)
        return dp[0]

