from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)

        # Step 1: Find the index of the MAXIMUM element
        l, r = 0, n - 1
        while l < r:
            m = (l + r + 1) // 2  # Ceiling division to prevent infinite loops when l = m
            if nums[m] > nums[l]:
                l = m
            else:
                r = m - 1

        max_idx = l
        min_idx = (max_idx + 1) % n  # The smallest element is right after the maximum

        # Step 2: Binary search using the virtual sorted array
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            real_m = (m + min_idx) % n  # Map virtual index to actual index

            if nums[real_m] == target:
                return real_m
            elif nums[real_m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1