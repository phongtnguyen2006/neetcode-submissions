from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        N = len(coins)

        def dfs(total: int, i: int) -> float:
            if total == amount:
                return 0
            if total > amount or i >= N:
                return float("inf")
            if (total, i) in memo:
                return memo[(total, i)]

            # Choice 1: take current coin (stay at index i since coins are infinite)
            keep = 1 + dfs(total + coins[i], i)

            # Choice 2: skip current coin (move to next index i + 1, do NOT add to total)
            skip = dfs(total, i + 1)

            memo[(total, i)] = min(keep, skip)
            return memo[(total, i)]

        ans = dfs(0, 0)
        return ans if ans != float("inf") else -1