class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(y, x, grid):
            dirs = [(0, 1),(0, -1),(1,0),(-1,0)]
            if grid[y][x] == '0':
                return False
            if grid[y][x] == '1':
                grid[y][x] = '0'
                for dy, dx in dirs:
                    if y + dy < len(grid) and  y + dy >= 0 and x + dx < len(grid[0]) and x + dx >= 0:
                        dfs(y + dy, x + dx, grid)

            
                return True
                

        ct = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if dfs(y, x, grid):
                    ct += 1
        return ct