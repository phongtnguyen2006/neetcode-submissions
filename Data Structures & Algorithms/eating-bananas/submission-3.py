class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        output = max(piles)

        while l <= r:
            ct = 0
            mid = (l + r) // 2
            print(mid)
            for num in piles:
                ct += (num // mid)
                if not num % mid == 0: ct += 1
            print(ct)
            if ct == h:
                output = mid
                r = mid - 1
            elif ct < h:
                r = mid - 1
                output = mid
            elif ct > h:
                l = mid + 1


        return output
    