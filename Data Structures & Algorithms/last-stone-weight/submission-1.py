class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = 0
            if stones:
                y = heapq.heappop(stones)
            print(x, y)
            if x == y:
                continue
            else:
                heapq.heappush(stones, x - y)
        if stones:
            return -stones[0]
        else:
            return 0