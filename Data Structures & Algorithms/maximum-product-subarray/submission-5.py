class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [(nums[0], nums[0])] + [(0, 0)] * (len(nums) - 1)
        max_product = nums[0]

        for i, num in enumerate(nums[1:], start = 1):
            
            max_val = max(max(num * dp[i - 1][0], num * dp[i - 1][1]), num)
            min_val = min(min(num * dp[i - 1][1], num * dp[i - 1][0]), num)
            dp[i] = (max_val, min_val)
            max_product = max(max_val, max_product)
        return max_product