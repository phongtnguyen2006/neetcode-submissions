class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        while 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                            if matrix[nr][nc] == 0:
                                break
                            matrix[nr][nc] = 2 ** 31
                            nr += dr
                            nc += dc
        nc += dc
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 2 ** 31:
                    matrix[r][c] = 0