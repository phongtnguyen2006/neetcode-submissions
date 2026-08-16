class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # mark visited
            area = 1

            for dy, dx in dirs:
                new_r, new_c = r + dy, c + dx
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    area += dfs(new_r, new_c)

            return area

        max_ct = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_ct = max(max_ct, dfs(r, c))

        return max_ct