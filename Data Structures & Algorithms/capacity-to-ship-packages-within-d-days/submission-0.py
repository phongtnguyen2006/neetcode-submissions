from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Search range must be from max(weights) to sum(weights)
        l = max(weights)
        r = sum(weights)

        while l < r:
            d = 1  # Start on day 1
            m = l + (r - l) // 2
            i = 0
            curr_total = 0

            while i < len(weights):
                if curr_total + weights[i] <= m:
                    curr_total += weights[i]
                    i += 1
                else:
                    d += 1
                    curr_total = 0
                    # Do NOT increment i here so weights[i] gets packed on the new day

            # If it fits within the allowed days, try to find a smaller capacity
            if d <= days:
                r = m
            else:
                l = m + 1

        return l