class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        iter each pos. if its a 1 start dfs/bfs. everytime check pos 
        chagne it to 2. add 1 to total
        """
        
        M, N = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sol = 0

        def bfs(r, c):            
            q = deque([(r, c)])
            while q:
                curr_r, curr_c = q.pop()
                grid[curr_r][curr_c] = '2'
                for dr, dc in dirs:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if 0 <= new_r < M and 0 <= new_c < N and grid[new_r][new_c] == '1':
                        q.append((new_r, new_c))

        for r in range(M):
            for c in range(N):
                if grid[r][c] == '1':
                    sol += 1
                    bfs(r, c)

        return sol


