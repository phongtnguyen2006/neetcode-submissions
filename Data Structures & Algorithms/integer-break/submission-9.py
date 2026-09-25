class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        sol = []

        while n > 4:
            sol.append(3)
            n -= 3

        sol.append(n)

        return math.prod(sol)