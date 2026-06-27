class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [2,12,8,3,10]
                at 8 add 8 + 2 or prev
        in dp list track max a pos

        '''

        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]
        dp.extend([0] * (len(nums) - 2))

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        print(dp)
        return max(dp[-1], dp[-2])

