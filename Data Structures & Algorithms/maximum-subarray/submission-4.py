class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] represents the maximum subarray sum ending at index i
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either extend the previous subarray or start fresh at nums[i]
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            max_sum = max(max_sum, dp[i])

        return max_sum