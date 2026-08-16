class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def bfs(r, c):
            if grid[r][c] == 0:
                return 0
            
            q = deque()
            q.append((r, c))
            visited.add((r,c))
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r = r + dr
                    new_c = c + dc
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        area += 1
            return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_area = max(bfs(r, c), max_area)

        return max_area



        