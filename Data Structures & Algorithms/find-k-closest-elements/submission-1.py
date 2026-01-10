from typing import List

class Solution:
    def findClosestElements(
        self, arr: List[int], k: int, x: int
    ) -> List[int]:
        left = 0
        total = sum(abs(arr[i] - x) for i in range(k))
        min_total = total

        for right in range(k, len(arr)):
            total -= abs(arr[right - k] - x)
            total += abs(arr[right] - x)

            # Keep the earlier window when totals are equal,
            # satisfying the smaller-element tie-break rule.
            if total < min_total:
                min_total = total
                left = right - k + 1

        return arr[left:left + k]