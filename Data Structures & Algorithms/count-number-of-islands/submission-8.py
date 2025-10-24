from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        M, N = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sol = 0

        def bfs(r, c):
            q = deque([(r, c)])  # Bug fix: wrap in a list so it holds a tuple
            grid[r][c] = '2'     # Bug fix: use '=' assignment and mark immediately

            while q:
                curr_r, curr_c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if 0 <= new_r < M and 0 <= new_c < N and grid[new_r][new_c] == '1':
                        grid[new_r][new_c] = '2'  # Mark visited immediately when pushed
                        q.append((new_r, new_c))

        for r in range(M):
            for c in range(N):
                if grid[r][c] == '1':
                    sol += 1  # Increment outside to keep BFS clean
                    bfs(r, c)

        return sol