class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        memo = {}
        def dfs(r, c):
            ct = 0                       # local to this cell, not nonlocal
            N, M = len(obstacleGrid), len(obstacleGrid[0])
            if obstacleGrid[r][c] == 1:
                return 0
            elif r == N - 1 and c == M - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]      # return this cell's stored count
            if 0 <= r + 1 < len(obstacleGrid):
                ct += dfs(r + 1, c)
            if 0 <= c + 1 < len(obstacleGrid[0]):
                ct += dfs(r, c + 1)
            memo[(r,c)] = ct
            return ct                    # this was missing -> None

        return dfs(0,0)                  # answer is what dfs(0,0) returns