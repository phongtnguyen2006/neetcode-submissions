class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] represents the minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for total in range(coin, amount + 1):
                dp[total] = min(dp[total], dp[total - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1