class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        extra_rotations = k % len(nums)
        
        for _ in range((extra_rotations)):
            end = nums[len(nums) - 1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = end
            
        return nums