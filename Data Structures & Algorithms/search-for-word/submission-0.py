# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         #base case: if length of curr word is same as word and not same then break
        
#         target_length = len(word)
#         visited = set()

#         def dfs(curr, i, x, y):
#             if curr[i] != word[i]:
#                 return False
#             if len(curr) == target_length and curr == word:
#                 return True
#             #check every direction. make sure have not visited cell already            
            
#             #check up and down
#             if 0 <= y - 1 < len(board) and (x, y - 1) not in visited:
#                 visited.add((x, y - 1))
#                 if dfs(curr + board[x][y - 1], i + 1, x, y - 1):
#                     return True
#             visited.remove((x, y - 1))
#             if 0 <= y + 1 < len(board)  and (x, y + 1) not in visited:
#                 visited.add((x, y + 1))
#                 if dfs(curr + board[x][y + 1], i + 1, x, y + 1):
#                     return True
#             visited.remove((x, y + 1))
#             #check left and right
#             if 0 <= x - 1 < len(board[i]) and (x - 1, y) not in visited:
#                 visited.add((x - 1, y))
#                 if dfs(curr + board[x - 1][y], i + 1, x, y + 1):
#                     return True
#             visited.remove((x - 1, y))
#             if 0 <= x + 1 < len(board[i]) and (x + 1, y) not in visited:
#                 visited.add((x + 1, y))
#                 if dfs(curr + board[x][y + 1], i + 1, x, y + 1):
#                     return True
#             visited.remove((x + 1, y))
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(board[i][j], 0, i, j):
#                     return True
        
#         return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        
