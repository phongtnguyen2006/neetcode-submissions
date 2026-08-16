class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        curr_total = 0
        def dfs(r, c):
            # if (r,c) in passed:
            #     return
            grid[r][c] = 0
            nonlocal curr_total
            curr_total += 1
            DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in DIRECTIONS:
                nr, nc = r + dx, c + dy
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    dfs(nr, nc)
            print(curr_total)
            return curr_total
            
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_total = 0
                    max_island = max(dfs(r,c), max_island)

        return max_island