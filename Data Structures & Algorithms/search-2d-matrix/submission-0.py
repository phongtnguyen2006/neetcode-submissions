class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        copy = []

        for l in matrix:
            copy = copy + l

        l = 0
        r = len(copy) - 1

        while l <= r:
            m = (l + r) // 2
            if copy[m] == target:
                return True
            elif copy[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False