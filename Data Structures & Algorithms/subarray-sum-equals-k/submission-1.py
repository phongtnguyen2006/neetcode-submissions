class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    
        pf = defaultdict(int)
        pf[0] = 1
        total = 0
        sol = 0
        for i, num in enumerate(nums):
            total += num
            if total - k in pf:
                sol += pf[total - k]
            pf[total] += 1

        print(pf)
        return sol
