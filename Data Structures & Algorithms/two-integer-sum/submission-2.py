class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        
        for i, num in enumerate(nums):
            if target - num in my_dict:
                return [my_dict[target - num], i]
            else:
                my_dict[num] = i
