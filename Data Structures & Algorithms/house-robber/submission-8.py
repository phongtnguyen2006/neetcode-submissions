class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [2,12,8,3,10]
                at 8 add 8 + 2 or prev
        in dp list track max a pos

        '''
        if len(nums) <= 2:
            return max(nums)

        dp = nums[:]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
            dp[i - 1] = max(dp[i - 1], dp[i - 2])

        print(dp)
        return dp[-1]