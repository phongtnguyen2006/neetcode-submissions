class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        minl, minr = 0, k - 1
        min_total = 0
        total = 0

        for i in range(0, k):
            total += abs(arr[i] - x)
        min_total = total

        for r in range(k, len(arr)):
            total -= abs(arr[r - k] - x)
            total += abs(arr[r] - x)

            if total < min_total:
                min_total = total
                
                minl, minr = r - k + 1, r
                print(minl, minr)
        return arr[minl:minr + 1]

