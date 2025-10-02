from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                curr_r, curr_c = q.popleft()

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    if (nr, nc) not in visited and 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    num_islands += 1
                    bfs(r, c)

        return num_islands
            



