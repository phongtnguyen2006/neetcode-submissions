import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        while l <  r:
            m = (l + r) // 2
            hrs = 0
            
            for i, num in enumerate(piles):
                hrs += math.ceil(num / m)

            if hrs <= h:
                r = m
            else:
                l = m + 1

        
        return r
