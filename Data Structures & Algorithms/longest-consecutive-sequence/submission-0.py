class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            s.add(num)

        max = 0

        for num in s:
            if num - 1 not in s:
                temp = num
                ct = 1
                while temp + 1 in s:
                    ct += 1
                    temp += 1
                if ct > max:
                    max = ct

        return max


        

        

