from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        check ct of 1 and 2 at beginning
        """
        q = deque()
        fresh = 0
        days = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1


        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dy, dx in dirs:
                    nr, nc = r + dy, c + dx
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            days += 1

        return days if fresh == 0 else -1



    


