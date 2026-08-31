class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        left = 0
        right = (len(nums) - 1)

        if len(nums) == 3 and (nums[0] + nums[1] + nums[2]) == 0:
            return [[nums[0], nums[1], nums[2]]]

        for i in range(1, len(nums) - 1):
            while left < i and right > i:
                sum = nums[left] + nums[i] + nums[right]
                if sum == 0:
                    output.add(tuple(sorted([nums[left], nums[i], nums[right]])))
                    left += 1
                    right -= 1
                elif sum > 0: right -= 1
                elif sum < 0: left += 1
            left = 0
            right = (len(nums) - 1)
                        

        return list(map(list, output))