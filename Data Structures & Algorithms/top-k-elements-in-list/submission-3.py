class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]        
        for num in nums:
            d[num] += 1

        for key in d:
            l = d[key]
            buckets[l].append(key)
        sol = []
        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                sol.append(num)
            if len(sol) == k:
                return sol
        
        return sol

        