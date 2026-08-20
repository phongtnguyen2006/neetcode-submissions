class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod
        
        total = []

        for i in range(len(nums)):
            total.append(prod(nums[0:i]) * prod(nums[i + 1:len(nums)]))

        return total
