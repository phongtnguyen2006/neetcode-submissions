class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        iter through each pos. if find a 0 start dfs. if a pos is on the edge then
        not surrounded. 
        """

        M, N = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(r, c):
            if board[r][c] == 'X':
                return
            
            visited = set()
            q = []
            q.append((r, c))
            visited.add((r, c))

            while q:
                curr_r, curr_c = q.pop()
                if curr_r == 0 or curr_r == M - 1 or curr_c == 0 or curr_c == N - 1:
                    return
                
                for dr, dc in dirs:
                    new_r = curr_r + dr
                    new_c = curr_c + dc
                    # print(0 <= new_r < M, 0 <= new_c < N, board[new_r][new_c] == 'O', )
                    if 0 <= new_r < M and 0 <= new_c < N and board[new_r][new_c] == 'O' and (new_r, new_c) not in visited:
                        
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

            # print(visited)
            for r, c in visited:
                board[r][c] = 'X'

        
        for r in range(M):
            for c in range(N):
                dfs(r,c)


        