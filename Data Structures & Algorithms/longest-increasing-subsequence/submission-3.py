class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        iterate each position
        dp array to track longest seq at an index
        """


        dp = [1] * len(nums) 
        sol = 1

        for i in range(1, len(nums)):
            curr_max = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    curr_max = max(curr_max, dp[j])
            
            dp[i] += curr_max
            sol = max(sol, dp[i])

        print(dp)
        return sol