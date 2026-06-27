class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        max_f = 0

        for i in range(len(nums)-1, 0, -1):
            ct = k
            same = 1
            for j in range(i - 1, -1, -1):
                ct -= (nums[i] - nums[j])  
                print(ct, nums[i] - nums[j])              
                if 0 == ct:
                    same += 1 
                    break
                elif ct > 0:
                    same += 1
                    print(same)
                else:
                    break
            max_f = max(max_f, same)

        return max_f

                