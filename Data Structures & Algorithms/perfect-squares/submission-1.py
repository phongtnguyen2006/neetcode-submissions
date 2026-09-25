class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, int(n ** 0.5) + 1):
            square = i * i

            for j in range(n + 1):
                copies = j // square
                remainder = j % square

                dp[j] = min(dp[j], copies + dp[remainder])

        return dp[n]