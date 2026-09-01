class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        self.memo = {}
        return self.dfs(0, 0)

    def dfs(self, r, c):
        if self.grid[r][c] == 1:
            return 0
        if r == len(self.grid) - 1 and c == len(self.grid[0]) - 1:
            return 1

        if (r, c) in self.memo:
            return self.memo[(r, c)]

        total = 0
        if r + 1 < len(self.grid):
            total += self.dfs(r + 1, c)
        if c + 1 < len(self.grid[0]):
            total += self.dfs(r, c + 1)

        self.memo[(r, c)] = total
        return total