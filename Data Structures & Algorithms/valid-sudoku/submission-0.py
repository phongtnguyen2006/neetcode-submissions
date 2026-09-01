class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)] 
        box = [set() for _ in range(9)] 


        for i in range(9):
            for j in range (9):
                if board[i][j] in rows[i]:
                    return False
                elif board[i][j] == '.':
                    pass
                else: 
                    rows[i].add(board[i][j])

                if board[j][i] in cols[i]:
                    return False
                elif board[j][i] == '.':
                    pass
                else:
                    cols[i].add(board[j][i])
        
                if board[i][j] in box[(i // 3) * 3 + (j // 3)]:
                    return False
                elif board[i][j] == '.':
                    pass
                else:
                    box[(i // 3) * 3 + (j // 3)].add(board[i][j])
        return True