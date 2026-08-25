class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        put marked spots in que first. 
        bfs at each position one iteration
        if number of rotted didnt change then exit loop

        if ct of fresh == count rotted then return minutes
        otherwise -1
        """
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(grid), len(grid[0])
        fresh_ct = 0
        rotted_ct = 0
        q = deque()
        days = 0

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    fresh_ct += 1
                elif grid[r][c] == 2:
                    q.append((r, c ))

        while q:
            state_change = False
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in DIRS:
                    new_r, new_c = r + dr, c + dc

                    if 0 <= new_r < M and 0 <= new_c < N and grid[new_r][new_c] == 1:  
                        state_change = True
                        grid[new_r][new_c] = 3
                        rotted_ct += 1
                        q.append((new_r, new_c))
            # print(grid)

            if state_change:
                days += 1
        
        if rotted_ct == fresh_ct:
            return days
        else:
            return - 1



