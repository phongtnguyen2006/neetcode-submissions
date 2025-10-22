class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        passed = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            island = False
            if (r, c) in passed:
                return False
            elif grid[r][c] == "1":
                passed.add((r, c))
                island = True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    dfs(nr, nc)

            return island

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and dfs(r, c):
                    result += 1

        return result