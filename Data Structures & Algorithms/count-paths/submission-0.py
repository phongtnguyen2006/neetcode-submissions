class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        [x, 15, 10, 6, 3, 1]
        [6, 5, 4, 3, 2, 1]
        [1, 1, 1, 1, 1, 0]

        """
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                if r + 1 < m: 
                    dp[r][c] += dp[r + 1][c]
                if c + 1 < n:
                    print(dp[r][c], dp[r][c + 1])
                    dp[r][c] += dp[r][c + 1]
        print(dp)
        return dp[0][0]