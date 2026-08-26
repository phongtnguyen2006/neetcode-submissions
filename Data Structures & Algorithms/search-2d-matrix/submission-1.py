class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            l1 = 0
            r1 = len(matrix[m]) - 1
            if target >= matrix[m][l1] and target <= matrix[m][r1]:
                while l1 <= r1:
                    m1 = (l1 + r1) // 2
                    if matrix[m][m1] == target:
                        return True
                    elif target > matrix[m][m1]:
                        l1 = m1 + 1
                    elif target < matrix[m][m1]:
                        r1 = m1 - 1
                return False
            elif target > matrix[m][l1]:
                l = m + 1
            elif target < matrix[m][r1]:
                r = m - 1


        return False