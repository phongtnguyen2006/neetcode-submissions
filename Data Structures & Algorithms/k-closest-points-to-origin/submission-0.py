class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        sol = []

        for x, y in points:
            heapq.heappush(heap, (math.sqrt(x ** 2 + y ** 2), (x, y)))

        for _ in range(k):
            sol.append(heapq.heappop(heap)[1])
        
        return sol