from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cache = set()
        cache.add(()) 
        
        def dfs(i, subset):
            nonlocal cache
            nonlocal nums
            # new_subset = 
            
            cache.add(subset)

            if i == len(nums) - 1:
                return
            dfs(i + 1, subset + (nums[i + 1],))
            dfs(i + 1, subset)
            
        for i in range(len(nums)):
            subset = (nums[i],)
            dfs(i, subset)

                
        return [list(x) for x in cache]